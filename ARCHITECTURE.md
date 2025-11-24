# Architecture Documentation

## Overview

This document describes the architecture of the Legal Document Assistant, a full-stack application featuring AI-powered legal document generation with SSE streaming and LLM function calling.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         Frontend                            │
│                    (Next.js 15.1.3)                         │
│                                                             │
│  ┌────────────────┐  ┌──────────────┐  ┌─────────────────┐  │
│  │ ChatInterface  │  │   Message    │  │ DocumentPreview │  │
│  │   Component    │  │  Component   │  │    Component    │  │
│  └────────────────┘  └──────────────┘  └─────────────────┘  │
│           │                 │                    │          │
│           └─────────────────┴───────────────────┘          │
│                             │                               │
│                      SSE EventSource                        │
└─────────────────────────────┬───────────────────────────────┘
                              │
                          HTTP/SSE
                              │
┌─────────────────────────────▼───────────────────────────────┐
│                         Backend                             │
│                      (Flask 3.0.0)                          │
│                                                             │
│  ┌────────────────────────────────────────────────────────┐ │
│  │                    Routes Layer                        │ │
│  │  ┌─────────┐  ┌────────────┐  ┌────────────────────┐   │ │
│  │  │ /health │  │   /chat    │  │ /conversations/:id │   │ │
│  │  └─────────┘  └────────────┘  └────────────────────┘   │ │
│  └────────────────────────────────────────────────────────┘ │
│                              │                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │                  Services Layer                        │ │
│  │  ┌──────────────────────┐  ┌────────────────────────┐  │ │
│  │  │  DocumentService     │  │ ConversationService    │  │ │
│  │  │  - generate()        │  │ - add_message()        │  │ │
│  │  │  - apply_edit()      │  │ - get_history()        │  │ │
│  │  └──────────────────────┘  └────────────────────────┘  │ │
│  └────────────────────────────────────────────────────────┘ │
│                              │                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │                    Models Layer                        │ │
│  │  ┌──────────────────────────────────────────────────┐  │ │
│  │  │         Function Schemas (FUNCTION_TOOLS)        │  │ │
│  │  │  - extract_information                           │  │ │
│  │  │  - generate_document                             │  │ │
│  │  │  - apply_edits                                   │  │ │
│  │  └──────────────────────────────────────────────────┘  │ │
│  └────────────────────────────────────────────────────────┘ │
│                              │                              │
└──────────────────────────────┼──────────────────────────────┘
                               │
                          Gemini API
                               │
┌──────────────────────────────▼───────────────────────────────┐
│                    Google Gemini Flash 2.5                   │
│                                                              │
│  - Function Calling                                          │
│  - Streaming Responses                                       │
│  - Context Management                                        │
└──────────────────────────────────────────────────────────────┘
```

## Backend Module Structure

### Layer Responsibilities

```
┌──────────────────────────────────────────────────────────┐
│ app.py (Entry Point)                                     │
│  - Application factory                                   │
│  - Blueprint registration                                │
│  - Server configuration                                  │
└────────────────────────┬─────────────────────────────────┘
                         │
    ┌────────────────────┼────────────────────┐
    │                    │                    │
    ▼                    ▼                    ▼
┌─────────┐      ┌──────────────┐    ┌──────────────┐
│ config  │      │   routes     │    │   models     │
│  .py    │◄─────┤   /chat.py   │    │  /schemas.py │
└─────────┘      └───────┬──────┘    └──────────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
         ▼               ▼               ▼
    ┌─────────┐   ┌──────────┐   ┌──────────┐
    │services │   │ prompts  │   │  utils   │
    │         │   │          │   │          │
    │document │   │ system_  │   │streaming │
    │convers. │   │ prompt   │   │  .py     │
    └─────────┘   └──────────┘   └──────────┘
```

### Module Details

#### 1. **app.py** (Entry Point)
- **Purpose**: Application initialization and configuration
- **Pattern**: Application factory
- **Responsibilities**:
  - Create Flask app instance
  - Configure CORS
  - Register blueprints
  - Start server

#### 2. **config.py** (Configuration)
- **Purpose**: Centralized configuration management
- **Contents**:
  - Environment variables
  - API keys
  - Server settings
  - Validation logic

#### 3. **routes/** (API Layer)
- **Purpose**: Handle HTTP requests and responses
- **Files**:
  - `chat.py`: Chat endpoints with SSE streaming
- **Responsibilities**:
  - Request validation
  - Response formatting
  - Stream management
  - Error handling

#### 4. **services/** (Business Logic)
- **Purpose**: Core application logic
- **Files**:
  - `document_service.py`: Document generation and editing
  - `conversation_service.py`: Conversation state management
- **Responsibilities**:
  - Document templates
  - Edit operations
  - State persistence
  - Data validation

#### 5. **models/** (Data Layer)
- **Purpose**: Data structures and schemas
- **Files**:
  - `schemas.py`: Function definitions for Gemini
- **Responsibilities**:
  - Function schemas
  - Data models
  - Type definitions

#### 6. **prompts/** (AI Configuration)
- **Purpose**: LLM prompt management
- **Files**:
  - `system_prompt.py`: System instructions
- **Responsibilities**:
  - Prompt templates
  - Instruction sets
  - Context definitions

#### 7. **utils/** (Utilities)
- **Purpose**: Shared helper functions
- **Files**:
  - `streaming.py`: SSE utilities
- **Responsibilities**:
  - SSE formatting
  - Common utilities
  - Helper functions

## Data Flow

### 1. User Sends Message

```
User Input → Frontend ChatInterface
           → POST /chat (SSE connection)
           → routes/chat.py
```

### 2. Backend Processing

```
routes/chat.py
  ↓
conversation_service.add_message() (store user message)
  ↓
Gemini Model (with FUNCTION_TOOLS and SYSTEM_PROMPT)
  ↓
Stream Response Chunks
  ↓
If function_call detected:
  ↓
  execute_function() in routes/chat.py
    ↓
    DocumentService.generate() or DocumentService.apply_edit()
      ↓
      conversation_service.set_document()
  ↓
  Send function result back to Gemini
  ↓
  Continue streaming
```

### 3. Response Streaming

```
SSE Stream:
  ├─ type: "text" → Display in chat
  ├─ type: "function_call" → Show function indicator
  ├─ type: "document" → Update document preview
  └─ type: "done" → End stream
```

## Communication Patterns

### SSE Streaming Protocol

```
Client                          Server
  │                               │
  ├──── POST /chat ──────────────►│
  │     { message, conv_id }      │
  │                               │
  │◄────data: {type:"text"}───────┤
  │◄────data: {type:"text"}───────┤
  │◄────data: {type:"function"}───┤
  │◄────data: {type:"document"}───┤
  │◄────data: {type:"text"}───────┤
  │◄────data: {type:"done"}───────┤
  │                               │
```

### Function Calling Flow

```
1. User Message
   ↓
2. Gemini analyzes message
   ↓
3. Gemini calls function (e.g., extract_information)
   ↓
4. Backend executes function
   ↓
5. Result sent back to Gemini
   ↓
6. Gemini generates natural language response
   ↓
7. Response streamed to frontend
```

## State Management

### Conversation State

```python
conversations = {
    "conv_id_1": [
        {"role": "user", "parts": ["I need an NDA"]},
        {"role": "model", "parts": ["I'll help you..."]}
    ]
}
```

### Document State

```python
documents = {
    "conv_id_1": "NON-DISCLOSURE AGREEMENT\n..."
}
```

## Design Patterns

### 1. **Application Factory Pattern**
- Used in `app.py`
- Enables testing and configuration flexibility

### 2. **Service Layer Pattern**
- Business logic separated into services
- Easy to test and maintain

### 3. **Blueprint Pattern**
- Routes organized into blueprints
- Scalable route management

### 4. **Singleton Pattern**
- `conversation_service` instance
- Single source of truth for state

### SSE Streaming
- **Benefit**: Immediate feedback, no buffering
- **Implementation**: Generator functions with yield

### In-Memory Storage
- **Benefit**: Fast access, no DB latency
- **Limitation**: Not persistent, single-instance only

### Async Processing
- **Current**: Synchronous with threading
- **Future**: Consider async/await for better concurrency
