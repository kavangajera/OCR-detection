import Vision
from Foundation import NSURL


def ocr_mac(img_path, recognition_level="accurate", languages=["en-US"]):
    results = []

    def handler(request, error):
        if error:
            return
        for obs in request.results():
            candidate = obs.topCandidates_(1)[0]
            results.append(candidate.string())
    
    request = Vision.VNRecognizeTextRequest.alloc().initWithCompletionHandler_(handler)

    request.setRecognitionLanguages_(languages)
    request.setRecognitionLevel_(
        Vision.VNRequestTextRecognitionLevelAccurate
        if recognition_level == "accurate"
        else Vision.VNRequestTextRecognitionLevelFast
    )

    handler = Vision.VNImageRequestHandler.alloc().initWithURL_options_(
        NSURL.fileURLWithPath_(img_path), None
    )

    handler.performRequests_error_([request], None)
    return "\n".join(results)
