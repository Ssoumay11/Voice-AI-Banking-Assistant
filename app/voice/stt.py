import speech_recognition as sr
from app.voice.mic import get_audio

def listen():
    recognizer = sr.Recognizer()

    audio = get_audio()

    if audio is None:
        return ""

    try:
        print("Processing...")
        text = recognizer.recognize_google(audio, language="en-IN")

        text = text.lower().strip()
        print(f"User: {text}")

        return text

    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""

    except sr.RequestError:
        print("API error")
        return ""