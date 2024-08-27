from detection.ObjectDetector import ObjectDetector
from rtsp_client.RtspClient import RtspClient
import time

# base_path = "C:/Alex/Dev/data_corpus/VideoCamera"


def test_cam():

    object_detector = ObjectDetector(size="m")
    rtsp_client = RtspClient.from_config_file('config.properties')
    time.sleep(1)
    desired_class_name = "person"

    for i in range(30):

        image_path = "./.out/" + str(i) + ".jpg"
        rtsp_client.save_screen(image_path)
        results = object_detector.predict(image_path)

        if ObjectDetector.is_there_object_class(results, desired_class_name):
            ObjectDetector.show_results(results)

    rtsp_client.close()


test_cam()

