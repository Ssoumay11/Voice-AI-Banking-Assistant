import speech_recognition as sr

def get_audio():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        # ✅ Adjust noise properly
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(
                source,
                timeout=10,              # more time to start speaking
                phrase_time_limit=7      # enough time to speak
            )
            return audio

        except sr.WaitTimeoutError:
            print("Listening timeout")
            return None