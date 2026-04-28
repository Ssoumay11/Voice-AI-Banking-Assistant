import json

USER_FILE = "app/data/dummy_db.json"
CURRENT_USER = "Soumay Verma"

def get_balance():
    try:
        with open(USER_FILE, "r") as f:
            users = json.load(f)

        for user in users:
            if user["name"] == CURRENT_USER:
                return user["balance"]

    except:
        pass

    return 0


def handle_balance():
    balance = get_balance()
    return f"Your current balance is {balance} rupees."