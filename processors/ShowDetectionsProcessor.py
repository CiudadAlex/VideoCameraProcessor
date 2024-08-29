from detection.ObjectDetector import ObjectDetector


class ShowDetectionsProcessor:

    def __init__(self, object_detector):
        self.object_detector = object_detector

    @classmethod
    def load_with_custom_model(cls, model_name):
        object_detector = ObjectDetector.load_custom_model(model_name=model_name)
        return cls(object_detector)

    @classmethod
    def load_with_standard_model(cls, size="x"):
        object_detector = ObjectDetector.load_standard_model(size=size)
        return cls(object_detector)

    def show_detections(self, list_image_path):

        for image_path in list_image_path:
            results = self.object_detector.predict(image_path)
            ObjectDetector.show_results(results)
