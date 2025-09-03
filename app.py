#!/usr/bin/env python3
import json
import random
import os
from flask import Flask, render_template, jsonify, request, send_from_directory
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

THINKERS_FILE = "thinkers.json"
SEEDS_FILE = "seeds.json"
PROMPT_FILE = "prompt.json"
CONFIG_FILE = "config.json"
PROVOCATIONS_FILE = "provocations.json"

API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

def load_json_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return [] if filename == PROVOCATIONS_FILE else {}

def save_provocations(provocations):
    with open(PROVOCATIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(provocations, f, indent=2, ensure_ascii=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/thinkers')
def get_thinkers():
    data = load_json_file(THINKERS_FILE)
    # Convert array format to dictionary format for the frontend
    if isinstance(data, dict) and 'thinkers' in data:
        thinkers_dict = {}
        for thinker in data['thinkers']:
            name = thinker.get('name', 'Unknown')
            thinkers_dict[name] = {
                'description': thinker.get('spirit_instruction', ''),
                'themes': [],
                'keywords': []
            }
        return jsonify(thinkers_dict)
    return jsonify(data)

@app.route('/api/provocations')
def get_provocations():
    return jsonify(load_json_file(PROVOCATIONS_FILE))

@app.route('/api/seeds')
def get_seeds():
    return jsonify(load_json_file(SEEDS_FILE))

@app.route('/api/prompt')
def get_prompt():
    return jsonify(load_json_file(PROMPT_FILE))

@app.route('/api/config')
def get_config():
    return jsonify(load_json_file(CONFIG_FILE))

@app.route('/api/generate', methods=['POST'])
def generate_provocation():
    if not API_KEY:
        return jsonify({"error": "API key not configured"}), 500
    
    data = request.json
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    
    system_prompt = data.get('systemPrompt', '')
    user_prompt = data.get('userPrompt', '')
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Combine system and user prompts
        full_prompt = f"{system_prompt}\n\n{user_prompt}"
        
        response = model.generate_content(full_prompt)
        
        if response.text:
            # Try to extract JSON from the response
            response_text = response.text.strip()
            # If the response has markdown code blocks, extract the JSON
            if '```json' in response_text:
                response_text = response_text.split('```json')[1].split('```')[0].strip()
            elif '```' in response_text:
                response_text = response_text.split('```')[1].split('```')[0].strip()
            
            try:
                result = json.loads(response_text)
            except json.JSONDecodeError:
                return jsonify({"error": "Invalid JSON response from AI"}), 500
            
            # Validate result structure
            if not isinstance(result, dict) or 'provocation' not in result:
                return jsonify({"error": "Invalid response format from AI"}), 500
            
            # Save to provocations file if it looks valid
            if 'provocation' in result:
                provocations = load_json_file(PROVOCATIONS_FILE)
                if not isinstance(provocations, list):
                    provocations = []
                provocations.append(result)
                save_provocations(provocations)
            
            return jsonify(result)
        else:
            return jsonify({"error": "No response from AI"}), 500
            
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print(f"Error generating provocation: {e}")
        print(f"Traceback: {error_detail}")
        return jsonify({"error": str(e), "detail": error_detail}), 500

@app.route('/api/vote', methods=['POST'])
def vote():
    data = request.json
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
        
    provocation_id = data.get('id')
    vote_value = data.get('vote')
    comment = data.get('comment', '')
    
    if provocation_id is None or vote_value is None:
        return jsonify({"error": "Missing id or vote"}), 400
    
    provocations = load_json_file(PROVOCATIONS_FILE)
    if not isinstance(provocations, list):
        return jsonify({"error": "Invalid provocations data structure"}), 500
    
    if 0 <= provocation_id < len(provocations):
        # Initialize feedback structure if it doesn't exist
        if 'feedback' not in provocations[provocation_id]:
            provocations[provocation_id]['feedback'] = []
        
        # Add new feedback entry
        from datetime import datetime
        feedback_entry = {
            'rating': vote_value,
            'comment': comment,
            'timestamp': datetime.now().isoformat()
        }
        provocations[provocation_id]['feedback'].append(feedback_entry)
        
        save_provocations(provocations)
        return jsonify({"success": True})
    
    return jsonify({"error": "Invalid provocation id"}), 400


if __name__ == '__main__':
    # Use environment variable for port (Render sets this)
    port = int(os.environ.get('PORT', 5000))
    # Disable debug in production
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug_mode)