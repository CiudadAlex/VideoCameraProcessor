from detection.ObjectDetector import ObjectDetector
from rtsp_client.RtspClient import RtspClient
import time

# base_path = "C:/Alex/Dev/data_corpus/VideoCamera"


def test_cam():

    object_detector = ObjectDetector(size="m")
    rtsp_client = RtspClient.from_config_file('config.properties')
    time.sleep(1)

    for i in range(10):

        image_path = "./.out/" + str(i) + ".jpg"
        rtsp_client.save_screen(image_path)
        results = object_detector.predict(image_path)

        ObjectDetector.show_results(results)

    rtsp_client.close()


test_cam()

