# Creative Acts Generator

A minimalist web application that generates thought-provoking creative acts inspired by various artistic and philosophical traditions.

## Overview

This app combines ideas from Situationism, Dadaism, Fluxus, and other creative movements to generate simple, actionable creative provocations. Each provocation consists of a poetic setup and a single physical task designed to shift your perspective on everyday life.

## Features

- **AI-Powered Generation**: Uses Google's Gemini AI to create unique provocations
- **Creative Traditions**: Draws from 25+ different creative thinkers and movements
- **Fully Customizable**: Edit seeds, prompts, and thinkers through simple JSON files
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
├── seeds.json            # Conceptual seeds for inspiration
├── prompt.json           # AI prompt templates (customizable!)
├── provocations.json     # Saved provocations
├── requirements.txt      # Python dependencies
└── .env                  # API keys (not in repo)
```

## How It Works

1. The app randomly selects a "guiding spirit" from your `thinkers.json` file
2. It picks a conceptual seed from your `seeds.json` collection
3. Using the templates in `prompt.json`, Gemini AI combines these elements
4. Each provocation includes:
   - A poetic setup sentence
   - One specific, physical task to perform

**The magic**: By editing the JSON files, you can completely customize the creative output!

## Examples

**Provocation**: "The city speaks in forgotten alphabets."  
**Task**: "Walk your usual route backwards, photographing only shadows cast by signs."

**Provocation**: "Empty rooms hold the weight of departed conversations."  
**Task**: "Sit in a public space for exactly 7 minutes, writing down only the last word you hear each minute."

**Want different styles?** Edit `seeds.json` and `thinkers.json` to create provocations that match your interests!

## Customizing Your Generator

This app is designed to be easily customizable! You can modify:

### **seeds.json** - Add Your Own Creative Seeds
Edit this file to add new conceptual starting points:
```json
{
  "seeds": [
    "The rhythm of everyday objects",
    "Your new creative seed here",
    "Another inspiring phrase"
  ]
}
```

### **thinkers.json** - Add New Creative Traditions
Add new creative movements, artists, or philosophers:
```json
{
  "thinkers": [
    {
      "name": "Your Creative Movement",
      "spirit_instruction": "Description of their creative approach..."
    }
  ]
}
```

### **prompt.json** - Customize AI Behavior
Advanced users can modify how the AI generates provocations:
- Edit the `system_prompt` to change generation rules
- Modify the `user_prompt_template` to change how seeds and thinkers combine
- **Important**: Keep the `{thinker_instruction}` and `{seed}` placeholders!

## Contributing

Feel free to fork and enhance! Some ideas:
- Create themed generation modes
- Build a gallery of favorite provocations
- Add social sharing features
- Create import/export for custom seed collections

## License

MIT