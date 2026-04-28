from app.voice.tts import speak
from app.utils.error_handler import safe_listen
from app.nlp.intent import detect_intent

from app.modules.balance import handle_balance
from app.modules.transfer import handle_transfer
from app.modules.cheque import handle_cheque
from app.modules.kyc import handle_kyc
import time
time.sleep(0.8)
def welcome():
    speak("Welcome to Kentiq AI Voice Bot from Dubai Bank Bank. How can I help you?")

def run():
    welcome()

    while True:
        command = safe_listen()

        if not command:
            continue

        intent = detect_intent(command)

        if intent == "balance":
            speak(handle_balance())

        elif intent == "transfer":
            speak("Starting money transfer process.")
            speak(handle_transfer())

        elif intent == "cheque":
            speak("Starting cheque verification.")
            speak(handle_cheque())

        elif intent == "kyc":
            speak("Starting KYC process.")
            speak(handle_kyc())

        else:
            speak("Sorry, I didn't understand that. Please try again.")

if __name__ == "__main__":
    run()