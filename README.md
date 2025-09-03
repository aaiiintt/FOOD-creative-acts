# Creative Acts Generator

A minimalist web application that generates thought-provoking creative acts inspired by various artistic and philosophical traditions.

## Overview

This app combines ideas from Situationism, Dadaism, Fluxus, and other creative movements to generate simple, actionable creative provocations. Each provocation consists of a poetic setup and a single physical task designed to shift your perspective on everyday life.

## Features

- **AI-Powered Generation**: Uses Google's Gemini AI to create unique provocations
- **Creative Traditions**: Draws from 25+ different creative thinkers and movements
- **Simple Interface**: Clean, minimal design focused on the provocations
- **Vote System**: Track which provocations resonate with thumbs up/down
- **Persistent Storage**: Saves all generated provocations to JSON

## Tech Stack

- **Backend**: Flask (Python) with Gunicorn WSGI server
- **AI**: Google Generative AI (Gemini)
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **Data**: JSON files for storage

## Installation

1. Clone the repository:
```bash
git clone https://github.com/aaiiintt/FOOD-creative-acts.git
cd FOOD-creative-acts
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your environment variables:
```bash
# Create .env file
echo 'GOOGLE_API_KEY="your_gemini_api_key_here"' > .env
```

Get your API key from: https://makersuite.google.com/app/apikey

## Usage

### Development Mode
Start the development server:
```bash
python3 app.py
```

### Production Mode (Recommended)
Start with Gunicorn for better performance:
```bash
gunicorn --workers 3 --bind 0.0.0.0:5000 wsgi:app
```

2. Open your browser and navigate to:
```
http://localhost:5000/
```

3. Click "Generate New Provocation" to create a creative act

## Project Structure

```
FOOD-creative-acts/
├── app.py                 # Flask application
├── wsgi.py               # Gunicorn entry point
├── templates/
│   └── index.html        # Web interface
├── thinkers.json         # Creative traditions data
├── provocations.json     # Saved provocations
├── requirements.txt      # Python dependencies
└── .env                  # API keys (not in repo)
```

## How It Works

1. The app randomly selects a "guiding spirit" from 25+ creative thinkers (Situationists, Dadaists, etc.)
2. It picks a conceptual seed from a curated list of 30 evocative phrases
3. Gemini AI combines these elements following strict rules to create a provocation
4. Each provocation includes:
   - A poetic setup sentence
   - One specific, physical task to perform

## Examples

**Provocation**: "The city speaks in forgotten alphabets."  
**Task**: "Walk your usual route backwards, photographing only shadows cast by signs."

**Provocation**: "Empty rooms hold the weight of departed conversations."  
**Task**: "Sit in a public space for exactly 7 minutes, writing down only the last word you hear each minute."

## Contributing

Feel free to fork and enhance! Some ideas:
- Add new thinkers to `thinkers.json`
- Expand the conceptual seeds list
- Create themed generation modes
- Build a gallery of favorite provocations
- Add social sharing features

## License

MIT