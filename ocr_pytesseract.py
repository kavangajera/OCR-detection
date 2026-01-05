import pytesseract
from PIL import Image


def ocr_pytesseract(img_path, lang="eng"):
    img = Image.open(img_path)
    text = pytesseract.image_to_string(img, lang=lang)
    return text.strip()
