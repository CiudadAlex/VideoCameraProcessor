from ultralytics import YOLO


class ObjectDetector:

    def __init__(self):
        self.model = YOLO("../yolov8x.pt")  # load an official model

    def predict(self, image_path):
        results = self.model.predict(source=image_path, conf=0.2)
        return results

