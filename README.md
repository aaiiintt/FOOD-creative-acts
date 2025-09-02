# FOOD-creative-acts

## Creative Acts to Make You Think

This project is a system designed to generate and display "creative acts" or thought-provoking prompts. It is now a single FastAPI application that handles both the web interface and AI-powered provocation generation.

## Features

*   **Provocation Generation**: Utilizes AI/LLM models to generate unique and thought-provoking creative acts.
*   **Web Interface**: A simple web-based interface to view existing provocations and trigger the generation of new ones.
*   **API Endpoints**: Provides API access to retrieve provocations and initiate the generation process.

## Technologies Used

### Frontend
*   HTML
*   JavaScript

### Backend (Python)
*   Python
*   FastAPI
*   Uvicorn (ASGI server)
*   Gunicorn (WSGI HTTP server)
*   LangChain (for LLM orchestration)
*   OpenAI (for AI model interaction)
*   python-dotenv (for environment variables)

### Data
*   JSON for storing provocations and scores.

## Setup and Installation

To set up and run this project locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/FOOD-creative-acts.git
cd FOOD-creative-acts
```

### 2. Python Backend Setup

It's recommended to use a virtual environment for Python dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Environment Variables

Create a `.env` file in the project root and add your Google API key:

```
GOOGLE_API_KEY="your_google_api_key_here"
```

### 4. Running the Application

Start the FastAPI application using Gunicorn:

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker generate:app
```

### 5. Accessing the Frontend

Once the backend is running, open your web browser and navigate to:

```
http://localhost:8000/
```

This will redirect you to `example.html`. You can also directly access:

```
http://localhost:8000/static/example.html
```
or

```
http://localhost:8000/static/test_interface.html
```

## Usage

*   **View Provocations**: The main interface will display a list of creative acts.
*   **Generate New**: Click the "Generate New Provocation" button (on `example.html`) to create a new thought-provoking prompt using the AI backend.

---

## Future Developments

This project is a foundation for exploring AI-generated creative content. We encourage contributions and forks to expand its capabilities! Here are some ideas for future development:

*   **User Authentication**: Implement user login and registration to personalize experiences.
*   **Provocation Curation**: Allow users to save, categorize, and share their favorite provocations.
*   **Advanced Scoring/Feedback**: Develop more sophisticated ways for users to provide feedback on provocations (e.g., upvoting/downvoting, detailed reviews).
*   **Diverse Generation Models**: Integrate support for different AI models or fine-tune existing ones for specific types of creative acts.
*   **Thematic Generation**: Enable users to request provocations based on specific themes or keywords.
*   **Improved UI/UX**: Enhance the frontend with a more dynamic and interactive user interface, potentially using a modern JavaScript framework (e.g., React, Vue, Svelte).
*   **Containerization**: Provide Docker support for easier deployment and environment management.
*   **Testing**: Expand test coverage for both backend and frontend components.

Feel free to fork this repository, implement your ideas, and contribute back to the community!