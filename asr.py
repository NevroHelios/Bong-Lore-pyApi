import requests
from dotenv import load_dotenv
import os

load_dotenv()

SARVAM_AI_API = os.environ.get("SARVAM_API_KEY")  # fixed key name

api_url = "https://api.sarvam.ai/speech-to-text"
headers = {"api-subscription-key": SARVAM_AI_API}

data = {"model": "saarika:v2.5", "with_diarization": False, "language_code": "bn-IN"}


def get_transcription(audio_bytes, filename, content_type):
    files = {"file": (filename, audio_bytes, content_type)}
    # try:
    resp = requests.post(api_url, headers=headers, data=data, files=files)
    resp.raise_for_status()
    json_resp = resp.json()
    transcript = json_resp.get("transcript", "")
    # except Exception as e:
    #     transcript = ""
    #     with open("log.txt", "a") as f:
    #         f.write(f"Error: {str(e)}\n")
    # else:
    #     with open("log.txt", "a") as f:
    #         f.write(f"Transcription response: {transcript}\n")
    return transcript
