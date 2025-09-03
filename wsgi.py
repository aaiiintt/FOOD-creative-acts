#!/usr/bin/env python3
"""
WSGI entry point for production deployment.
This file tells Gunicorn where to find the Flask application instance.
"""

from app import app

if __name__ == "__main__":
    app.run()