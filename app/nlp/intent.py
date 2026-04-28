def detect_intent(text: str) -> str:
    if not text:
        return "unknown"

    text = text.lower()

    if any(word in text for word in ["balance", "account balance", "check balance"]):
        return "balance"

    elif any(word in text for word in ["transfer", "send", "pay"]):
        return "transfer"

    elif any(word in text for word in ["cheque", "check cheque", "scan cheque", "upload cheque"]):
        return "cheque"

    elif "kyc" in text:
        return "kyc"

    return "unknown"