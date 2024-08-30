from processors.VideoCameraClassImageSaverProcessor import VideoCameraClassImageSaverProcessor
from processors.ShowDetectionsProcessor import ShowDetectionsProcessor
from detection.ModelGenerator import ModelGenerator


execute_action = "VideoCameraClassImageSaverProcessor"
base_path = "C:/Alex/Dev/data_corpus/VideoCamera"


if execute_action == "ShowDetectionsProcessor":
    show_detections_processor = ShowDetectionsProcessor.load_with_custom_model(model_name="lightnings")
    show_detections_processor.show_detections(list_image_path=[base_path + "/lightning.jpg"])

if execute_action == "VideoCameraClassImageSaverProcessor":
    video_camera_class_image_saver_processor = VideoCameraClassImageSaverProcessor.load_with_custom_model(model_name="birds")
    video_camera_class_image_saver_processor.save_images_with_class(desired_class_name="bird", show_in_screen=True)

if execute_action == "ModelGenerator":
    path_train = base_path + "/vidar.v2i.yolov8/data.yaml"
    results = ModelGenerator.train_new_model(model_path="./.models/yolov8n.pt", yaml_path=path_train, epochs=20)
    print(results)
