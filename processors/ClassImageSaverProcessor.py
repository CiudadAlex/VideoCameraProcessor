from detection.ObjectDetector import ObjectDetector
from rtsp_client.RtspClient import RtspClient
from utils.KeyboardInterrupter import KeyboardInterrupter
import time


class ClassImageSaverProcessor:

    def __init__(self, object_detector):
        self.object_detector = object_detector
        self.rtsp_client = RtspClient.from_config_file('config.properties')

        # To allow the client to connect correctly
        time.sleep(1)

    @classmethod
    def load_with_custom_model(cls, model_name):
        object_detector = ObjectDetector.load_custom_model(model_name=model_name)
        return cls(object_detector)

    @classmethod
    def load_with_standard_model(cls, size="x"):
        object_detector = ObjectDetector.load_standard_model(size=size)
        return cls(object_detector)

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
