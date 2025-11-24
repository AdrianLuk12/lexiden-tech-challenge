# Legal Document Assistant - Backend

Flask backend with SSE streaming and Gemini API integration.

## Setup

1. Install Python 3.13.5 or higher
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create `.env` file:
   ```bash
   cp .env.example .env
   ```

4. Add your Gemini API key to `.env`:
   ```
   GEMINI_API_KEY=your_actual_api_key
   ```

## Running

```bash
python app.py
```

Server will run on `http://localhost:5000`

## API Endpoints

- `GET /health` - Health check
- `POST /chat` - Main chat endpoint (SSE streaming)
- `GET /conversations/<id>` - Get conversation history
- `DELETE /conversations/<id>` - Delete conversation

## Function Calling

The backend implements three functions for the LLM:

1. **extract_information** - Extract structured data from conversation
2. **generate_document** - Generate legal documents
3. **apply_edits** - Apply edits to existing documents

## Supported Documents

- Director Appointment Resolutions
- Non-Disclosure Agreements (NDA)
- Employment Agreements
