from detection.ObjectDetector import ObjectDetector
from rtsp_client.RtspClient import RtspClient
import time


class ClassImageSaverProcessor:

    @staticmethod
    def save_images_with_class(desired_class_name):

        object_detector = ObjectDetector.load_standard_model(size="m")
        rtsp_client = RtspClient.from_config_file('config.properties')

        # To allow the client to connect correctly
        time.sleep(1)
        i = 0

        while True:

            pil_image = rtsp_client.get_pil_image()

            results = object_detector.predict(pil_image)

            if ObjectDetector.is_there_object_class(results, desired_class_name):
                ObjectDetector.show_results(results)
                image_path = "./.out/" + desired_class_name + "_" + str(i) + ".jpg"
                pil_image.save(image_path)

            print(f"iteration = {i}")
            i = i + 1

        rtsp_client.close()

    # FIXME pulir