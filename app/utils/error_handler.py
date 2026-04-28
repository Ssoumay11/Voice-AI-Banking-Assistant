from app.voice.tts import speak
from app.voice.stt import listen

def safe_listen(retries=3):
    for _ in range(retries):
        text = listen()
        if text:
            return text
        speak("Sorry, I didn't understand that. Please repeat.")
    return ""

def safe_speak(text):
    try:
        speak(text)
    except Exception:
        print("TTS failed")