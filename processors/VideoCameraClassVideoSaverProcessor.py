from detection.ObjectDetector import ObjectDetector
from rtsp_client.RtspClient import RtspClient
from utils.KeyboardInterrupter import KeyboardInterrupter
from utils.ObjectDetectorContainer import ObjectDetectorContainer
from camera_movement.CameraMovement import CameraMovement
from utils.TimeRegulator import TimeRegulator
from utils.ImageUtils import ImageUtils
from utils.CycleQueue import CycleQueue
from camera_movement.Tracker import Tracker
import time
import threading
import logging


class VideoCameraClassVideoSaverProcessor(ObjectDetectorContainer):

    def __init__(self, object_detector):
        super().__init__(object_detector)
        self.rtsp_client = RtspClient.from_config_file('config.properties')
        self.camera_movement = CameraMovement.from_config_file(config_file='config.properties')
        self.cycle_queue = CycleQueue(100)
        self.recording = False
        self.count_not_detection_to_finish_video = 0
        self.video_id = 0

        # To allow the client to connect correctly
        time.sleep(1)

    def action_on_close(self):
        print("Closing connection with camera...")
        self.rtsp_client.close()
        print("Connection with camera closed")

    def save_videos_with_class(self, desired_class_name, show_in_screen=True, path_output="./.out",
                               max_not_detection_to_finish_video=10, track=False):

        keyboard_interrupter = KeyboardInterrupter(self.action_on_close)
        keyboard_interrupter.start()

        thread_save_images_in_cycle_queue = threading.Thread(target=self.save_images_in_cycle_queue)
        thread_save_images_in_cycle_queue.start()

        thread_save_images_in_cycle_queue = \
            threading.Thread(target=self.detect_last_image_in_queue,
                             args=(desired_class_name, show_in_screen, path_output, max_not_detection_to_finish_video, track))
        thread_save_images_in_cycle_queue.start()

    def save_images_in_cycle_queue(self):

        time_regulator = TimeRegulator(interval_millis=40)

        while True:

            pil_image = self.rtsp_client.get_pil_image()
            self.cycle_queue.add(pil_image)
            time_regulator.wait_until_next_milestone()

    def detect_last_image_in_queue(self, desired_class_name, show_in_screen, path_output, max_not_detection_to_finish_video, track):

        while True:

            pil_image = self.cycle_queue.get_last_item()

            if pil_image is None:
                time.sleep(1)
                continue

            results = self.object_detector.predict(pil_image)

            if ObjectDetector.is_there_object_class(results, desired_class_name):

                logging.debug("Detection")

                if show_in_screen:
                    ObjectDetector.show_results(results)

                if track:
                    bounding_box = ObjectDetector.get_bounding_box_vertices_of_single_object_of_class(results, desired_class_name)
                    if bounding_box is not None:
                        (rectangle_up_left_position, rectangle_down_right_position) = bounding_box
                        width, height = pil_image.size
                        traker = Tracker(width, height, self.camera_movement)
                        traker.track(rectangle_up_left_position, rectangle_down_right_position)

                self.recording = True
                self.count_not_detection_to_finish_video = 0

                # Positive detection. Start recording everything
                self.cycle_queue.remove_limit_max_size()

            elif self.recording and self.count_not_detection_to_finish_video < max_not_detection_to_finish_video:
                self.count_not_detection_to_finish_video = self.count_not_detection_to_finish_video + 1
                logging.debug(f"count_not_detection_to_finish_video = {self.count_not_detection_to_finish_video}")

            elif self.recording:

                logging.debug(f"Write mp4 = {self.video_id}")
                self.recording = False
                list_images_pil = self.cycle_queue.get_all_and_reset()
                ImageUtils.generate_mp4(f"{path_output}/{desired_class_name}_{self.video_id}.mp4", list_images_pil)
                self.video_id = self.video_id + 1

