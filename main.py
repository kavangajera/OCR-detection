import time

from ocr_vision import ocr_mac
from ocr_easyocr import ocr_easyocr
from ocr_pytesseract import ocr_pytesseract
from accuracy_calc import evaluate_ocr


def benchmark(name, ocr_fn, img_path, gt):
    # warm-up
    ocr_fn(img_path)

    start = time.perf_counter()
    result = evaluate_ocr(ocr_fn, img_path, gt)
    elapsed = (time.perf_counter() - start) * 1000

    print(f"---- {name} ----")
    print("Prediction     :", result["prediction"])
    print("Char Accuracy  :", f"{result['char_accuracy']*100.0:.2f} %")
    print("Exact Match    :", "✅" if result["exact_match"] else "❌")
    print(f"Time Taken     : {elapsed:.2f} ms\n")

    return elapsed, result


if __name__ == "__main__":
    img_path = "images/card.png"

    
    ground_truth = """"""


    print("Evaluating OCR engines...\n")

    benchmark("Apple Vision OCR", ocr_mac, img_path, ground_truth)
    benchmark("PyTesseract OCR", ocr_pytesseract, img_path, ground_truth)
    benchmark("EasyOCR (CPU)", ocr_easyocr, img_path, ground_truth)
