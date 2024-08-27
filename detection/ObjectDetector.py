from ultralytics import YOLO


class ObjectDetector:

    def __init__(self, size="x"):

        available_sizes = ["n", "s", "m", "l", "x"]

        if size not in available_sizes:
            raise Exception(f"Unrecognized model size: {size}. Available sizes: {available_sizes}")

        self.model = YOLO(".models/yolov8" + size + ".pt")  # load an official model

    def predict(self, image_path):
        results = self.model.predict(source=image_path, conf=0.2)
        return results

