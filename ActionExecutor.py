from processors.VideoCameraClassImageSaverProcessor import VideoCameraClassImageSaverProcessor
from processors.VideoCameraClassVideoSaverProcessor import VideoCameraClassVideoSaverProcessor
from processors.ShowDetectionsProcessor import ShowDetectionsProcessor
from detection.ModelGenerator import ModelGenerator
from detection.ObjectDetector import ObjectDetector


class ActionItem:

    def __init__(self, model_name, desired_class_name, example_image, train_dir, show_in_screen, train_base_model, epochs):
        self.model_name = model_name
        self.desired_class_name = desired_class_name
        self.example_image = example_image
        self.train_dir = train_dir
        self.show_in_screen = show_in_screen
        self.train_base_model = train_base_model
        self.epochs = epochs


class ActionExecutor:

    base_path = "C:/Alex/Dev/data_corpus/VideoCamera"

    map_target_2_action_item = {
        "LIGHTNINGS": ActionItem("lightnings", "Lightning", "lightning.jpg", "vidar.v2i.yolov8", True, "yolov8n", 50),
        "BIRDS":      ActionItem("birds_gpu_40_epoch", "bird", "birds.jpg", "bird detection.v5i.yolov8", True, "yolov8n", 50),
        "PEOPLE":     ActionItem("yolov8n", "person", "", "", True, "yolov8n", 50)
    }

    list_actions_available = ["ShowDetectionsProcessor", "VideoCameraClassImageSaverProcessor",
                              "VideoCameraClassVideoSaverProcessor", "ModelGenerator"]

    @staticmethod
    def validate(execute_action, target):

        if execute_action not in ActionExecutor.list_actions_available:
            raise Exception(f"Invalid action '{execute_action}'. Available actions: {ActionExecutor.map_target_2_action_item.keys()}")

        if target not in ActionExecutor.map_target_2_action_item:
            raise Exception(f"Invalid target '{target}'. Available targets: {ActionExecutor.map_target_2_action_item.keys()}")

    @staticmethod
    def get_object_detector(action_item):

        model_name = action_item.model_name
        object_detector = ObjectDetector.load_custom_model(model_name=model_name)
        return object_detector

    @staticmethod
    def exec_show_detections_processor(action_item):

        example_image = action_item.example_image
        object_detector = ActionExecutor.get_object_detector(action_item)
        show_detections_processor = ShowDetectionsProcessor(object_detector)
        show_detections_processor.show_detections(list_image_path=[ActionExecutor.base_path + "/" + example_image])

    @staticmethod
    def exec_video_camera_class_image_saver_processor(action_item):

        desired_class_name = action_item.desired_class_name
        show_in_screen = action_item.show_in_screen
        object_detector = ActionExecutor.get_object_detector(action_item)
        video_camera_class_image_saver_processor = VideoCameraClassImageSaverProcessor(object_detector)
        video_camera_class_image_saver_processor.save_images_with_class(desired_class_name=desired_class_name,
                                                                        show_in_screen=show_in_screen)

    @staticmethod
    def exec_video_camera_class_video_saver_processor(action_item):

        desired_class_name = action_item.desired_class_name
        show_in_screen = action_item.show_in_screen
        object_detector = ActionExecutor.get_object_detector(action_item)
        video_camera_class_video_saver_processor = VideoCameraClassVideoSaverProcessor(object_detector)
        video_camera_class_video_saver_processor.save_videos_with_class(desired_class_name=desired_class_name,
                                                                        show_in_screen=show_in_screen)

    @staticmethod
    def exec_model_generator(action_item):

        train_dir = action_item.train_dir
        train_base_model = action_item.train_base_model
        epochs = action_item.epochs
        path_train = ActionExecutor.base_path + "/" + train_dir + "/data.yaml"
        results = ModelGenerator.train_new_model(model_path=f"./.models/{train_base_model}.pt",
                                                 yaml_path=path_train,
                                                 epochs=epochs)
        print(results)

    @staticmethod
    def execute(execute_action, target):

        ActionExecutor.validate(execute_action, target)

        action_item = ActionExecutor.map_target_2_action_item[target]

        if execute_action == "ShowDetectionsProcessor":
            ActionExecutor.exec_show_detections_processor(action_item)

        if execute_action == "VideoCameraClassImageSaverProcessor":
            ActionExecutor.exec_video_camera_class_image_saver_processor(action_item)

        if execute_action == "VideoCameraClassVideoSaverProcessor":
            ActionExecutor.exec_video_camera_class_video_saver_processor(action_item)

        if execute_action == "ModelGenerator":
            ActionExecutor.exec_model_generator(action_item)
