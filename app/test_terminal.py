from app.nlp.intent import detect_intent
from app.modules.balance import handle_balance
from app.modules.transfer import handle_transfer
from app.modules.cheque import handle_cheque
from app.modules.kyc import handle_kyc


def run_test():
    print("=== TEXT TEST MODE ===")
    print("Type commands like: balance, transfer, cheque, kyc")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            break

        intent = detect_intent(user_input)

        if intent == "balance":
            print("Bot:", handle_balance())

        elif intent == "transfer":
            print("Bot: Starting transfer...")

            # simulate inputs manually
            name = input("Enter beneficiary name: ")
            bank = input("Enter bank name: ")
            account = input("Enter account number: ")
            amount = input("Enter amount: ")

            # simulate transfer_flow output
            result = {
                "status": "success",
                "name": name,
                "bank": bank,
                "account": "XXXX" + account[-4:],
                "amount": int(amount)
            }

            print("Bot: Processing transaction...")

            # temporarily inject into handler
            from app.modules.transfer import save_transaction
            import time

            transaction_data = {
                "timestamp": int(time.time()),
                "sender": "Soumay Verma",
                "receiver": name,
                "bank": bank,
                "account": "XXXX" + account[-4:],
                "amount": int(amount),
                "status": "success"
            }

            save_transaction(transaction_data)

            print("Bot: Transaction successful")

        elif intent == "cheque":
            print("Bot:", handle_cheque())

        elif intent == "kyc":
            print("Bot:", handle_kyc())

        else:
            print("Bot: Sorry, I didn't understand.")


if __name__ == "__main__":
    run_test()