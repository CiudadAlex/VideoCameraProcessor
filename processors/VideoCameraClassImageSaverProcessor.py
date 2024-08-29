from detection.ObjectDetector import ObjectDetector
from rtsp_client.RtspClient import RtspClient
from utils.KeyboardInterrupter import KeyboardInterrupter
from utils.ObjectDetectorContainer import ObjectDetectorContainer
import time


class VideoCameraClassImageSaverProcessor(ObjectDetectorContainer):

    def __init__(self, object_detector):
        super().__init__(object_detector)
        self.rtsp_client = RtspClient.from_config_file('config.properties')

        # To allow the client to connect correctly
        time.sleep(1)

    def action_on_close(self):
        print("Closing connection with camera...")
        self.rtsp_client.close()
        print("Connection with camera closed")

    def save_images_with_class(self, desired_class_name, show_in_screen=True):

        keyboard_interrupter = KeyboardInterrupter(self.action_on_close)
        keyboard_interrupter.start()

        i = 0

        while True:

            pil_image = self.rtsp_client.get_pil_image()

            results = self.object_detector.predict(pil_image)

            if ObjectDetector.is_there_object_class(results, desired_class_name):

                if show_in_screen:
                    ObjectDetector.show_results(results)

                image_path = "./.out/" + desired_class_name + "_" + str(i) + ".jpg"
                pil_image.save(image_path)

            print(f"iteration = {i}")
            i = i + 1
