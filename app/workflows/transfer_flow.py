from app.voice.stt import listen
from app.voice.tts import speak

import time

def ask(prompt):
    for _ in range(3):
        speak(prompt)

        time.sleep(1)   # 
        response = listen()

        if response:
            return response

        speak("I didn't catch that. Please speak clearly.")

    return ""


def confirm(prompt):
    speak(prompt + " Please say yes or no.")
    response = listen()

    if "yes" in response:
        return True
    elif "no" in response:
        return False
    else:
        speak("Please say yes or no.")
        return confirm(prompt)


def transfer_flow():
    # Step 1: Beneficiary Name
    name = ask("Please say the beneficiary name")

    # Step 2: Bank Name
    bank = ask("Please say the bank name")

    # Step 3: Account Number (masked)
    account = ask("Please say the account number")
    masked_account = "XXXX" + account[-4:] if len(account) >= 4 else "XXXX"

    # Step 4: Amount
    amount = ask("Please say the amount to transfer")

    # Step 5: Confirmation
    summary = f"You want to transfer {amount} rupees to {name} at {bank}, account ending with {masked_account}."
    
    if confirm(summary):
        speak("Processing your transaction. Please wait.")
        return {
            "status": "success",
            "message": "Transaction successful"
    }
    else:
        return {
            "status": "cancelled",
            "message": "Transaction cancelled"
        }