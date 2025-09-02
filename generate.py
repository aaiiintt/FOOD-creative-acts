import json
import os
import random
import time
import google.generativeai as genai
from google.api_core import exceptions as google_exceptions

# --- CONFIGURATION ---
NUM_PROVOCATIONS_TO_GENERATE = 200
PAUSE_BETWEEN_REQUESTS = 0.3
THINKERS_FILE = "thinkers.json"
OUTPUT_FILE = "provocations.json"

# --- CONFIGURE SDK ---
try:
    API_KEY = os.getenv("GOOGLE_API_KEY")
    if not API_KEY:
        raise ValueError("GOOGLE_API_KEY not found in environment variables.")
    genai.configure(api_key=API_KEY)
except ValueError as e:
    print(f"Error: {e}")
    print("Please set the GOOGLE_API_KEY environment variable before running the script.")
    exit()

# --- HELPER FUNCTIONS ---

def load_thinkers():
    """Loads the thinkers data from the JSON file."""
    try:
        with open(THINKERS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)["thinkers"]
    except FileNotFoundError:
        print(f"Error: The file '{THINKERS_FILE}' was not found.")
        exit()
    except (json.JSONDecodeError, KeyError):
        print(f"Error: The file '{THINKERS_FILE}' is not a valid or correctly formatted JSON file.")
        exit()

def load_existing_provocations():
    """Loads existing provocations from the output file to allow resuming."""
    try:
        with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_provocations(provocations):
    """Saves the list of provocations to the output file."""
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(provocations, f, indent=2, ensure_ascii=False)

# --- CORE GENERATION LOGIC ---

def generate_one_provocation(thinker):
    """Generates a single provocation using the Google AI SDK."""
    spirit_instruction = thinker['spirit_instruction']
    seed = random.choice(thinker['seeds'])

    system_prompt = f"""You are a generator of small, poetic, and actionable creative provocations. You translate a dense artistic concept into a simple, everyday task. You will return a JSON object with two keys: "setup" and "task".

    // --- PRIMARY DIRECTIVES ---
    **1. The "Anti-Homework" Mandate:** The task must NEVER feel like homework. It must avoid long-form writing or complex research.
    **2. The "Simplicity Filter":** The core task must be a single, elegant action explainable in one sentence.
    **3. The "Artifact Guarantee":** Every task MUST result in a small, simple physical or digital artifact (a photo, a note, a drawing).
    **4. The "Weirdness" Bias:** Favor the slightly strange or subversive option.

    // --- CORE RULES ---
    - The "setup" must be a single, short, poetic sentence.
    - The task must be a physical, tangible action.
    - Forbid abstract tasks like "imagine" or "consider".
    - NEVER mention the original source, person, or use any special jargon.

    **SPECIAL INSTRUCTION FOR THIS GENERATION (The 'Guiding Spirit'):**
    // {thinker['name']} //
    {spirit_instruction}"""
    
    user_prompt = f"""Based on the following conceptual seed, generate a creative provocation that follows all the rules, especially the 'Guiding Spirit' instruction. 
    
    CONCEPTUAL SEED: \"\"\"{seed}\"\"\""""

    model = genai.GenerativeModel(
        'gemini-2.5-flash',
        system_instruction=system_prompt
    )

    response = model.generate_content(
        user_prompt,
        generation_config={
            "response_mime_type": "application/json",
        }
    )
    
    if response.text:
        return json.loads(response.text)
    return None

# --- MAIN EXECUTION BLOCK ---

if __name__ == "__main__":
    thinkers = load_thinkers()
    generated_provocations = load_existing_provocations()
    seen_tasks = {p['task'] for p in generated_provocations}
    
    print(f"Found {len(generated_provocations)} existing provocations.")
    print(f"Goal is to generate {NUM_PROVOCATIONS_TO_GENERATE} total.")

    backoff_time = 5

    try:
        while len(generated_provocations) < NUM_PROVOCATIONS_TO_GENERATE:
            random_thinker = random.choice(thinkers)
            
            try:
                new_provocation = generate_one_provocation(random_thinker)

                if new_provocation and 'task' in new_provocation:
                    if new_provocation['task'] not in seen_tasks:
                        # Add to in-memory state
                        seen_tasks.add(new_provocation['task'])
                        generated_provocations.append(new_provocation)
                        
                        # --- KEY CHANGE: Save immediately to disk for robustness ---
                        save_provocations(generated_provocations)
                        
                        progress = len(generated_provocations)
                        print(f"({progress}/{NUM_PROVOCATIONS_TO_GENERATE}) Saved: {new_provocation['task'][:80]}...")
                        
                        time.sleep(PAUSE_BETWEEN_REQUESTS)
                        backoff_time = 5 # Reset backoff after a success
                    else:
                        print("Duplicate detected. Skipping.")
                else:
                     print("Generation failed (empty response). Retrying...")

            except google_exceptions.ResourceExhausted as e:
                print(f"Rate limit hit. Waiting for {backoff_time} seconds before retrying...")
                time.sleep(backoff_time)
                backoff_time *= 2
            except Exception as e:
                print(f"\nAn unexpected error occurred: {e}. Retrying after 10 seconds...")
                time.sleep(10)

    except KeyboardInterrupt:
        print("\n\nProcess interrupted by user.")
    finally:
        # Final save as a safeguard, though the file should already be up-to-date.
        print(f"Finalizing... saving {len(generated_provocations)} provocations to '{OUTPUT_FILE}'...")
        save_provocations(generated_provocations)
        print("✅ Done.")