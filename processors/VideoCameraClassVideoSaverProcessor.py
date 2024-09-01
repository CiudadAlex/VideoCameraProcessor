from detection.ObjectDetector import ObjectDetector
from rtsp_client.RtspClient import RtspClient
from utils.KeyboardInterrupter import KeyboardInterrupter
from utils.ObjectDetectorContainer import ObjectDetectorContainer
from utils.TimeRegulator import TimeRegulator
import time


class VideoCameraClassVideoSaverProcessor(ObjectDetectorContainer):

    def __init__(self, object_detector):
        super().__init__(object_detector)
        self.rtsp_client = RtspClient.from_config_file('config.properties')

        # To allow the client to connect correctly
        time.sleep(1)

    def action_on_close(self):
        print("Closing connection with camera...")
        self.rtsp_client.close()
        print("Connection with camera closed")

    def save_images_with_class(self, desired_class_name, show_in_screen=True, path_output="./.out"):

        keyboard_interrupter = KeyboardInterrupter(self.action_on_close)
        keyboard_interrupter.start()

        time_regulator = TimeRegulator(interval_millis=40)

        i = 0

        start = time.time()

        for i in range(100):

            pil_image = self.rtsp_client.get_pil_image()
            time_regulator.wait_until_next_milestone()

            i = i + 1
            print(".")

        end = time.time()
        seconds = end - start
        freq = 100 / seconds
        print(">>>>> " + str(freq) + " per second")
