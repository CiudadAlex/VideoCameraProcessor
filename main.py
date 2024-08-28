from detection.ObjectDetector import ObjectDetector
from rtsp_client.RtspClient import RtspClient
import time

base_path = "C:/Alex/Dev/data_corpus/VideoCamera"


def test_bird():
    object_detector = ObjectDetector.load_custom_model(model_name="birds")
    image_path = base_path + "/birds.jpg"
    results = object_detector.predict(image_path)
    ObjectDetector.show_results(results)


def test_cam():

    object_detector = ObjectDetector.load_standard_model(size="m")
    rtsp_client = RtspClient.from_config_file('config.properties')
    time.sleep(1)
    desired_class_name = "person"

    for i in range(100):

        pil_image = rtsp_client.get_pil_image()

        results = object_detector.predict(pil_image)

        if ObjectDetector.is_there_object_class(results, desired_class_name):
            ObjectDetector.show_results(results)
            image_path = "./.out/" + str(i) + ".jpg"
            pil_image.save(image_path)

        print(f"iteration = {i}")

    rtsp_client.close()


# test_cam()
test_bird()


