import cv2
import os
from app.voice.tts import speak

IMAGE_PATH = "assets/images/cheque.jpg"


# ---------- VALIDATION ----------
def validate_cheque(image_path):
    # 1️ Check file exists
    if not os.path.exists(image_path):
        return False, "No image found"

    # 2️ Check if image is supported/readable
    img = cv2.imread(image_path)
    if img is None:
        return False, "Unsupported or corrupted image format"

    h, w, _ = img.shape
    print(f"[DEBUG] Image size: {w}x{h}")

    # 3️ Check if image is not too small
    if h < 50 or w < 50:
        return False, "Image too small"

    #  Accept as valid (mock system)
    return True, "Cheque accepted"


# HANDLER
def handle_cheque():
    speak("Please upload a cheque image in the images folder as cheque dot jpg.")

    valid, message = validate_cheque(IMAGE_PATH)

    if valid:
        speak("Cheque verification successful.")
        return "Cheque verified successfully."

    else:
        speak("Cheque verification failed.")
        return f"Cheque verification failed. {message}"