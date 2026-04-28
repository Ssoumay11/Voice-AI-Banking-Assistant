def normalize_bank_name(text):
    text = text.lower()

    if "sbi" in text:
        return "State Bank of India"
    if "hdfc" in text:
        return "HDFC Bank"
    if "icici" in text:
        return "ICICI Bank"

    return text.title()