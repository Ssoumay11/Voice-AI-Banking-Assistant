import json
import time
from app.workflows.transfer_flow import transfer_flow

TRANSACTION_FILE = "app/data/transactions.json"
USER_FILE = "app/data/dummy_db.json"
CURRENT_USER = "Soumay Verma"


# ---------- JSON Helpers ----------
def read_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return []


def write_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


# ---------- User Handling ----------
def get_user():
    users = read_json(USER_FILE)

    for user in users:
        if user["name"] == CURRENT_USER:
            return user, users

    return None, users


# ---------- Balance Update ----------
def update_balance(users, updated_user):
    for i, user in enumerate(users):
        if user["name"] == updated_user["name"]:
            users[i] = updated_user
            break

    write_json(USER_FILE, users)


# ---------- Transaction Save ----------
def save_transaction(data):
    transactions = read_json(TRANSACTION_FILE)
    transactions.append(data)
    write_json(TRANSACTION_FILE, transactions)


# ---------- Main Transfer ----------
def handle_transfer():
    result = transfer_flow()

    user, users = get_user()

    if not user:
        return "User not found."

    amount = result.get("amount", 0)

    # ❌ INVALID AMOUNT
    if amount <= 0:
        return "Invalid amount entered."

    # ❌ INSUFFICIENT BALANCE
    if user["balance"] < amount:
        transaction_data = {
            "timestamp": int(time.time()),
            "sender": CURRENT_USER,
            "receiver": result.get("name", ""),
            "bank": result.get("bank", ""),
            "amount": amount,
            "status": "failed - insufficient balance"
        }

        save_transaction(transaction_data)

        return "Insufficient balance. Transaction failed."

    # ✅ SUCCESS → Deduct balance
    user["balance"] -= amount
    update_balance(users, user)

    transaction_data = {
        "timestamp": int(time.time()),
        "sender": CURRENT_USER,
        "receiver": result.get("name", ""),
        "bank": result.get("bank", ""),
        "account": result.get("account", ""),
        "amount": amount,
        "status": "success"
    }

    save_transaction(transaction_data)

    return f"Transaction successful. Your remaining balance is {user['balance']} rupees."