# image_to_text_libs.py
# Library Management for OCR

import pytesseract
from PIL import Image

def text_from_image(image_path):
    """Extract text from an image using pytesseract."""
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return fp"