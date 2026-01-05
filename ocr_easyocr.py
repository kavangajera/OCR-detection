import easyocr


def ocr_easyocr(img_path, languages=["en"]):
    reader = easyocr.Reader(languages, gpu=False)
    results = reader.readtext(img_path, detail=0)
    return "\n".join(results)
