from ultralytics import YOLO
import math


class ObjectDetector:

    def __init__(self, size="x"):

        available_sizes = ["n", "s", "m", "l", "x"]

        if size not in available_sizes:
            raise Exception(f"Unrecognized model size: {size}. Available sizes: {available_sizes}")

        self.model = YOLO(".models/yolov8" + size + ".pt")  # load an official model

    def predict(self, image_path):
        results = self.model.predict(source=image_path, conf=0.7)
        return results

    @staticmethod
    def is_there_object_class(results, class_name):

        for r in results:
            boxes = r.boxes

            for box in boxes:

                # class name
                cls = int(box.cls[0])
                class_name_box = r.names[cls]

                if class_name_box == class_name:
                    return True

        return False

    @staticmethod
    def print_results(results):

        for r in results:
            boxes = r.boxes

            for box in boxes:
                # bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # convert to int values

                confidence = math.ceil((box.conf[0] * 100)) / 100

                # class name
                cls = int(box.cls[0])

                print(f"Class name: {r.names[cls]}. Confidence: {confidence}"
                      f". Window ---> (x1, y1) = ({x1}, {y1}), (x2, y2) = ({x2}, {y2})")

    @staticmethod
    def show_results(results):
        for r in results:
            r.show()  # Display the image with predictions
