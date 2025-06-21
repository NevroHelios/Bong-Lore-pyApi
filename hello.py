from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import logging
import io
import base64
from pydantic import BaseModel

from asr import get_transcription
from agent import chat_agent
from tts import text_to_speech


class RequestModel(BaseModel):
    inputs: str


class Progress:
    def __init__(self) -> None:
        self.status = "transcripting"

    def update(self, status: str):
        self.status = status


progress = Progress()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.post("/get_transcript")
async def get_transcript(audio: UploadFile = File(...)):
    progress.update("transcripting")

    audio_bytes = await audio.read()
    response = get_transcription(audio_bytes, audio.filename, audio.content_type)

    progress.update("transcripted")

    return {
        "message": "success",
        "data": response,
    }


@app.post("/chat_response")
async def generate(request: RequestModel):
    progress.update("generating response")

    response = chat_agent(request.inputs)

    progress.update("response generated")

    return {
        "message": "success",
        "data": response,
    }


@app.post("/text_to_speech")
def text_to_speech2(request: RequestModel):
    progress.update("generating audio")

    audio = text_to_speech(
        target_language_code="bn-IN",
        text=request.inputs,
        model="bulbul:v2",
        speaker="anushka",
    )
    progress.update("audio generated")

    audio_b64 = base64.b64encode(audio).decode("ascii")
    return {"message": "success", "data": audio_b64}



@app.get("/progress")
def get_progress():
    return {"status": progress.status}
