from sarvamai import SarvamAI
# from sarvamai.play import play
# from elevenlabs import play
from dotenv import load_dotenv
import os
import base64
load_dotenv()


client = SarvamAI(api_subscription_key=os.getenv("SARVAM_API_KEY"))

def text_to_speech(text, target_language_code="bn-IN", model="bulbul:v2", speaker="anushka"):

    cumulative_audio_bytes = []
    chunk_size = 1000
    # Correctly chunk the text into parts of 1000 characters
    for i in range(0, len(text), chunk_size):
        text_chunk = text[i:i + chunk_size]
        response = client.text_to_speech.convert(
            target_language_code=target_language_code,
            text=text_chunk,
            model=model,
            speaker=speaker
        )
        for audio_b64 in response.audios:
            # audio_b64 = audio_tuple[0]  # Extract the base64 string from the tuple
            cumulative_audio_bytes.append(base64.b64decode(audio_b64))
    # print(cumulative_audio_bytes[:100])
    # print(f"Total audio bytes: {len(cumulative_audio_bytes)}")
    return b"".join(cumulative_audio_bytes)


if __name__ == "__main__":

    audio = text_to_speech(
        target_language_code="bn-IN",
        text="আমি একটি বৃহৎ ভাষা মডেল, গুগল দ্বারা প্রশিক্ষিত।",
        model="bulbul:v2",
        speaker="anushka"
    )

    # play(audio)
