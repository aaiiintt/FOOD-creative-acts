import json
from flask import Flask, jsonify, send_from_directory

# --- CONFIGURATION ---
PROVOCATIONS_FILE = "provocations.json"

# --- FLASK APP SETUP ---
app = Flask(__name__, static_url_path='')

def load_json_file(filename, default_value):
    """Safely loads a JSON file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default_value

# --- API ENDPOINTS ---

@app.route('/')
def serve_index():
    """Serves the main testing interface HTML file."""
    return send_from_directory('.', 'test_interface.html')

@app.route('/get_all_provocations')
def get_all_provocations():
    """
    CHANGED: This now sends the entire deck of provocations to the client.
    The client will handle shuffling and state.
    """
    all_provocations = load_json_file(PROVOCATIONS_FILE, [])
    return jsonify(all_provocations)

# REMOVED: The /vote endpoint is no longer needed as voting is handled client-side.

# --- RUN THE SERVER ---
if __name__ == '__main__':
    print("Starting the testing server...")
    print("Open your browser and go to http://127.0.0.1:5000")
    # debug=False is better for a production-like test
    app.run(debug=False, port=5000)