from rapidfuzz.distance import Levenshtein


def char_accuracy(ground_truth: str, prediction: str) -> float:
    """
    Character-level accuracy based on Levenshtein distance.
    Accuracy = 1 - (edit_distance / len(ground_truth))
    """
    if not ground_truth:
        return 0.0

    dist = Levenshtein.distance(ground_truth, prediction)
    return max(0.0, 1 - dist / len(ground_truth))


def exact_match(ground_truth: str, prediction: str) -> int:
    """
    Exact match accuracy (1 if fully correct, else 0)
    """
    return int(ground_truth == prediction)


def evaluate_ocr(ocr_fn, img_path: str, ground_truth: str) -> dict:
    """
    Runs OCR, calculates accuracy metrics, and returns results.
    """
    pred = ocr_fn(img_path)

    return {
        "prediction": pred,
        "char_accuracy": char_accuracy(ground_truth, pred),
        "exact_match": exact_match(ground_truth, pred)
    }
