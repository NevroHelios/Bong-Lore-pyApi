# Bengali Virtual Assistant API

A FastAPI-based backend for a Bengali virtual assistant, supporting speech-to-text, text-to-speech, and intelligent chat responses. Designed for Bengali speakers, especially those in Kolkata, with a focus on local context and easy language.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [API Routes](#api-routes)
- [Usage](#usage)
- [License](#license)

## Introduction
This project provides a RESTful API for:
- Converting Bengali speech to text using Sarvam AI
- Generating Bengali speech from text
- Chatting with a Bengali language model (Gemini)

## Features
- Bengali speech-to-text (ASR)
- Bengali text-to-speech (TTS)
- Bengali chat agent with local context
- CORS enabled for easy frontend integration

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/NevroHelios/Bong-Lore-pyApi
   cd Bong-Lore-pyApi
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up environment variables:**
   - Create a `.env` file in the root directory with the following keys:
     ```env
     SARVAM_API_KEY=your_sarvam_api_key
     GEMINI_API_KEY=your_gemini_api_key
     ```

## Environment Variables
- `SARVAM_API_KEY`: API key for Sarvam AI (ASR & TTS)
- `GEMINI_API_KEY`: API key for Gemini chat agent

## API Routes

### `GET /`
- Health check. Returns a welcome message.

### `POST /get_transcript`
- **Description:** Convert uploaded Bengali audio to text.
- **Request:** `multipart/form-data` with `audio` file
- **Response:**
  ```json
  { "message": "success", "data": "<transcript>" }
  ```

### `POST /chat_response`
- **Description:** Get a Bengali chat response.
- **Request:** JSON `{ "inputs": "<your question in Bengali>" }`
- **Response:**
  ```json
  { "message": "success", "data": "<response>" }
  ```

### `POST /text_to_speech`
- **Description:** Convert Bengali text to speech (audio, base64 encoded).
- **Request:** JSON `{ "inputs": "<text in Bengali>" }`
- **Response:**
  ```json
  { "message": "success", "data": "<base64-audio>" }
  ```

### `GET /progress`
- **Description:** Get current processing status.
- **Response:** `{ "status": "<status>" }`

## Usage
- Run the server:
  ```bash
  uvicorn hello:app --reload
  ```
  or
  ```bash
  fastapi run hello.py
  ```
- Use tools like Postman or cURL to interact with the endpoints.
- Integrate with your frontend for Bengali voice assistant features.

## License
MIT License
