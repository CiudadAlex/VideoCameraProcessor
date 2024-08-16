from ObjectDetector import ObjectDetector


base_path = "C:/Alex/Dev/data_corpus/VideoCamera"


def predict(obj_detector, image_name):

    print("#####################################")
    result = obj_detector.predict(base_path + "/" + image_name)
    print(result)


object_detector = ObjectDetector()

predict(object_detector, "person1.jpg")
predict(object_detector, "car1.jpg")
predict(object_detector, "dog1.jpg")
predict(object_detector, "cat1.jpg")

