from detection.ObjectDetector import ObjectDetector
from utils.ObjectDetectorContainer import ObjectDetectorContainer


class ShowDetectionsProcessor(ObjectDetectorContainer):

    def show_detections(self, list_image_path):

        for image_path in list_image_path:
            results = self.object_detector.predict(image_path)
            ObjectDetector.show_results(results)
