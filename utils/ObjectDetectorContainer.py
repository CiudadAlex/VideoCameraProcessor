from detection.ObjectDetector import ObjectDetector


class ObjectDetectorContainer:

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

    # FIXME use in processors
