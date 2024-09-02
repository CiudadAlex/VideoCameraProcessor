from detection.ObjectDetector import ObjectDetector
from rtsp_client.RtspClient import RtspClient
from utils.KeyboardInterrupter import KeyboardInterrupter
from utils.ObjectDetectorContainer import ObjectDetectorContainer
from utils.TimeRegulator import TimeRegulator
from utils.ImageUtils import ImageUtils
from utils.CycleQueue import CycleQueue
import time
import threading


class VideoCameraClassVideoSaverProcessor(ObjectDetectorContainer):

    def __init__(self, object_detector):
        super().__init__(object_detector)
        self.rtsp_client = RtspClient.from_config_file('config.properties')
        self.cycle_queue = CycleQueue(100)
        self.recording = False

        # To allow the client to connect correctly
        time.sleep(1)

    def action_on_close(self):
        print("Closing connection with camera...")
        self.rtsp_client.close()
        print("Connection with camera closed")

    def save_images_with_class(self, desired_class_name, show_in_screen=True, path_output="./.out"):

        keyboard_interrupter = KeyboardInterrupter(self.action_on_close)
        keyboard_interrupter.start()

        thread_save_images_in_cycle_queue = threading.Thread(target=self.save_images_in_cycle_queue)
        thread_save_images_in_cycle_queue.start()

        # FIXME call thread with detect_las_image_in_queue

    def save_images_in_cycle_queue(self):

        time_regulator = TimeRegulator(interval_millis=40)

        while True:

            pil_image = self.rtsp_client.get_pil_image()
            self.cycle_queue.add(pil_image)
            time_regulator.wait_until_next_milestone()

    # FIXME finish
    def detect_las_image_in_queue(self, desired_class_name, show_in_screen=True, path_output="./.out"):

        while True:

            pil_image = self.cycle_queue.get_last_item()
            results = self.object_detector.predict(pil_image)

            if ObjectDetector.is_there_object_class(results, desired_class_name):

                if show_in_screen:
                    ObjectDetector.show_results(results)

                self.recording = True

                # Positive detection. Start recording everything
                self.cycle_queue.remove_limit_max_size()

            elif self.recording:

                self.recording = False
                list_images_pil = self.cycle_queue.get_all_and_reset()
                ImageUtils.generate_gif(".out/desired_class_name.gif", list_images_pil)
