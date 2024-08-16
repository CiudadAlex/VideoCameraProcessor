from ObjectDetector import ObjectDetector
import math

base_path = "C:/Alex/Dev/data_corpus/VideoCamera"


def predict(obj_detector, image_name):

    print("#####################################")
    results = obj_detector.predict(base_path + "/" + image_name)

    for r in results:

        boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # convert to int values

            confidence = math.ceil((box.conf[0] * 100)) / 100

            # class name
            cls = int(box.cls[0])

            print(f"Class name: {r.names[cls]}. Confidence: {confidence}. Window ---> (x1, y1) = ({x1}, {y1}), (x2, y2) = ({x2}, {y2})")


object_detector = ObjectDetector()

predict(object_detector, "person1.jpg")

'''
predict(object_detector, "bus1.jpg")
predict(object_detector, "car1.jpg")
predict(object_detector, "dog1.jpg")
predict(object_detector, "cat1.jpg")
'''
