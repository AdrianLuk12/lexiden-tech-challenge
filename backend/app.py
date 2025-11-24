"""
Legal Document Assistant - Main Application Entry Point

A Flask-based backend for AI-powered legal document generation
with SSE streaming and LLM function calling.

This modular version is organized into:
- config.py: Configuration and environment variables
- models/: Data schemas and function definitions
- prompts/: System prompts
- services/: Business logic for documents and conversations
- routes/: API endpoints
- utils/: Helper utilities

For the monolithic version, see app.py.backup
"""
from flask import Flask
from flask_cors import CORS

from config import Config
from routes import chat_bp


def create_app():
    """
    Application factory pattern.

    Returns:
        Configured Flask application
    """
    # Initialize Flask app
    app = Flask(__name__)

    # Configure CORS
    CORS(app, origins=Config.CORS_ORIGINS)

    # Register blueprints
    app.register_blueprint(chat_bp)

    return app


# Create app instance
app = create_app()


if __name__ == '__main__':
    print("=" * 60)
    print("Legal Document Assistant API")
    print("=" * 60)
    print(f"Environment: {Config.FLASK_ENV}")
    print(f"Debug: {Config.FLASK_DEBUG}")
    print(f"Model: {Config.GEMINI_MODEL}")
    print(f"Starting server on http://{Config.HOST}:{Config.PORT}")
    print("=" * 60)
    print()

    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.FLASK_DEBUG,
        threaded=True
    )
