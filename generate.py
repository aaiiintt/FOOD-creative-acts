import json
import os
import random
import time
import google.generativeai as genai
from google.api_core import exceptions as google_exceptions
from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- CONFIGURATION ---
THINKERS_FILE = "thinkers.json"
PROVOCATIONS_FILE = "provocations.json"

# --- CONFIGURE SDK ---
try:
    API_KEY = os.getenv("GOOGLE_API_KEY")
    if not API_KEY:
        raise ValueError("GOOGLE_API_KEY not found in environment variables.")
    genai.configure(api_key=API_KEY)
except ValueError as e:
    print(f"Error: {e}")
    print("Please set the GOOGLE_API_KEY environment variable before running the script.")
    # Exit is not appropriate for a web server, but we'll log and let it fail on API call
    # For now, we'll just print and proceed, API calls will fail if key is missing

# --- FastAPI App Initialization ---
app = FastAPI()

# Mount static files from the current directory
app.mount("/static", StaticFiles(directory="."), name="static")

# --- Helper Functions (adapted for API context) ---

def load_provocations():
    """Loads existing provocations from the JSON file."""
    try:
        with open(PROVOCATIONS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def load_thinkers():
    """Loads the thinkers data from the JSON file."""
    try:
        with open(THINKERS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)["thinkers"]
    except FileNotFoundError:
        print(f"Warning: The file '{THINKERS_FILE}' was not found. Generation might be limited.")
        return []
    except (json.JSONDecodeError, KeyError):
        print(f"Warning: The file '{THINKERS_FILE}' is not a valid or correctly formatted JSON file.")
        return []

# --- API Endpoints ---

@app.get("/")
async def read_root():
    """Redirects to the example HTML page."""
    return FileResponse("example.html", media_type="text/html")

@app.get("/provocations")
async def get_provocations():
    """Returns the list of provocations."""
    return JSONResponse(content=load_provocations())

class GenerateRequest(BaseModel):
    systemPrompt: str
    userPrompt: str

@app.post("/generate-provocation")
async def generate_provocation_endpoint(request: GenerateRequest):
    """Generates a single provocation using the Google AI SDK based on provided prompts."""
    if not API_KEY:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Gemini API key not configured on the server."
        )

    model = genai.GenerativeModel(
        'gemini-2.5-flash',
        system_instruction=request.systemPrompt
    )

    try:
        response = model.generate_content(
            request.userPrompt,
            generation_config={
                "response_mime_type": "application/json",
            }
        )
        
        if response.text:
            return JSONResponse(content=json.loads(response.text))
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Gemini API returned an empty response."
            )

    except google_exceptions.ResourceExhausted:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit hit. Please try again later."
        )
    except Exception as e:
        print(f"An unexpected error occurred during generation: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate provocation: {e}"
        )

# You can keep the original script's bulk generation logic as a separate function
# or remove it if it's no longer needed for the web application.
# For now, I'm removing the __main__ block to make this purely a FastAPI app.
