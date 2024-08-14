from ultralytics import YOLO


class ObjectDetector:

    def __init__(self):
        self.model = YOLO("yolov8n-cls.pt")  # load an official model

    def predict(self, image_path):
        results = self.model(image_path)
        return results

