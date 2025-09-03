# Overview

This is a minimalist web application that generates creative acts and provocations inspired by various artistic and philosophical traditions. The app uses Google's Gemini AI to create unique creative challenges based on movements like Situationism, Dadaism, and Fluxus. Users can generate new provocations, vote on them with thumbs up/down, and all generated content is persistently stored in JSON files.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Backend Architecture
- **Framework**: Flask (Python) with a simple, single-file structure
- **AI Integration**: Google Generative AI (Gemini) for provocation generation
- **Configuration**: Environment variables loaded via python-dotenv
- **Production Server**: Gunicorn WSGI server with dedicated entry point (wsgi.py)

## Frontend Architecture
- **Technology**: Vanilla HTML/CSS/JavaScript (no frameworks)
- **Design Philosophy**: Minimalist, clean interface using monospace fonts
- **Styling**: Inline CSS in HTML template with dark theme (#1d1212 background, white content boxes)
- **User Interaction**: Simple voting system and generation triggers

## Data Storage
- **Persistence**: JSON file-based storage (no database)
- **Files**: 
  - `provocations.json`: Stores all generated provocations with voting data
  - `thinkers.json`: Contains creative traditions and their associated prompts/seeds
- **Data Structure**: Provocations include text, tasks, reflections, and vote counts

## API Design
- **Endpoints**: RESTful JSON API for frontend communication
- **Routes**:
  - `/` - Main application interface
  - `/api/thinkers` - Returns available creative traditions/thinkers
- **Data Flow**: Frontend requests → Flask routes → Gemini AI → JSON storage → Response

## Content Generation System
- **Creative Sources**: 25+ different artistic movements and thinkers
- **Generation Logic**: AI prompts based on selected creative tradition characteristics
- **Output Format**: Structured provocations with tasks and reflection questions

# External Dependencies

## AI Services
- **Google Generative AI (Gemini)**: Core content generation service
- **Authentication**: API key-based authentication via environment variables

## Python Libraries
- **Flask**: Web framework and templating
- **google-generativeai**: Official Google AI SDK
- **python-dotenv**: Environment variable management
- **Gunicorn**: Production WSGI server

## Configuration Requirements
- **Environment Variables**: `GOOGLE_API_KEY` for Gemini AI access
- **API Access**: Requires Google MakerSuite API key
- **No Database**: Self-contained with file-based persistence