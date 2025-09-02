import json
from flask import Flask, jsonify, request, send_from_directory

# --- CONFIGURATION ---
PROVOCATIONS_FILE = "provocations.json"
SCORES_FILE = "/data/provocations_scores.json"

# --- FLASK APP SETUP ---
app = Flask(__name__, static_url_path='')

def load_json_file(filename, default_value):
    """Safely loads a JSON file, returning a default if it doesn't exist."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default_value

def save_json_file(filename, data):
    """Saves data to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# --- API ENDPOINTS ---

@app.route('/')
def serve_index():
    """Serves the main testing interface HTML file."""
    return send_from_directory('.', 'test_interface.html')

@app.route('/get_unvoted_provocations')
def get_unvoted_provocations():
    """
    Returns a list of all provocations that haven't been scored yet.
    This allows a tester to pick up where they left off.
    """
    all_provocations = load_json_file(PROVOCATIONS_FILE, [])
    scores = load_json_file(SCORES_FILE, [])
    
    # Create a set of tasks that have already been scored for fast lookup
    scored_tasks = {score['task'] for score in scores}
    
    # Filter out any provocations that are already in the scores file
    unvoted = [p for p in all_provocations if p['task'] not in scored_tasks]
    
    return jsonify(unvoted)

@app.route('/vote', methods=['POST'])
def handle_vote():
    """
    Receives a vote, adds it to the scores file, and saves it.
    """
    vote_data = request.json
    print(f"Received vote: {vote_data['vote']} for task: {vote_data['task'][:40]}...")

    scores = load_json_file(SCORES_FILE, [])
    
    # Create the new score entry
    new_score = {
        "setup": vote_data['setup'],
        "task": vote_data['task'],
        "vote": vote_data['vote'] # "up" or "down"
    }
    
    scores.append(new_score)
    save_json_file(SCORES_FILE, scores)
    
    return jsonify({"status": "success", "message": "Vote recorded."})


# --- RUN THE SERVER ---
if __name__ == '__main__':
    print("Starting the testing server...")
    print("Open your browser and go to http://127.0.0.1:5000")
    app.run(debug=True, port=5000)