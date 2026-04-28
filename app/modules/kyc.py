import os
import time
import sounddevice as sd
from scipy.io.wavfile import write, read
import cv2
import speech_recognition as sr
from app.voice.tts import speak

KYC_FOLDER = "app/data/kyc_records/"


#  AUDIO RECORD 
def record_audio(duration=5, filename="kyc_audio.wav"):
    fs = 44100

    speak("Please say the following sentence clearly after the beep.")
    speak("This is Soumay Verma for KYC verification.")

    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    filepath = os.path.join(KYC_FOLDER, filename)
    write(filepath, fs, recording)

    return filepath


#  AUDIO PLAYBACK 
def play_audio(filepath):
    fs, data = read(filepath)
    sd.play(data, fs)
    sd.wait()


#  AUDIO TRANSCRIPTION 
def transcribe_audio(file_path):
    r = sr.Recognizer()

    with sr.AudioFile(file_path) as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio, language="en-IN")
        return text.lower()
    except:
        return ""


#  VIDEO RECORD 
def record_video(duration=5, filename="kyc_video.avi"):
    speak("Recording video. Please look at the camera.")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return None

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    filepath = os.path.join(KYC_FOLDER, filename)

    out = cv2.VideoWriter(filepath, fourcc, 20.0, (640, 480))

    start_time = time.time()

    while int(time.time() - start_time) < duration:
        ret, frame = cap.read()

        if ret:
            out.write(frame)
            cv2.imshow("KYC Video Recording", frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    return filepath


#  MAIN HANDLER 
def handle_kyc():
    if not os.path.exists(KYC_FOLDER):
        os.makedirs(KYC_FOLDER)

    speak("Starting KYC process. We will record your audio and video.")

    timestamp = int(time.time())

    audio_file = f"kyc_audio_{timestamp}.wav"
    video_file = f"kyc_video_{timestamp}.avi"

    try:
        #  Record audio
        audio_path = record_audio(5, audio_file)

        #  Playback
        speak("Playing back your recorded audio.")
        play_audio(audio_path)

        #  Transcription check
        text = transcribe_audio(audio_path)
        print("KYC Audio Text:", text)

        expected = "this is soumay verma for kyc verification"

        if expected in text:
            speak("KYC audio verified successfully.")
        else:
            speak("Could not clearly verify your statement, but continuing process.")

        #  Record video
        video_path = record_video(5, video_file)

        if audio_path and video_path:
            return "KYC completed successfully. Audio and video have been recorded."

        elif audio_path:
            return "Audio recorded but video failed."

        elif video_path:
            return "Video recorded but audio failed."

        else:
            return "KYC failed completely."

    except Exception as e:
        print("KYC Error:", e)
        return "KYC failed due to a system error."