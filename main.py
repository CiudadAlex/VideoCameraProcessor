from processors.VideoCameraClassImageSaverProcessor import VideoCameraClassImageSaverProcessor
from processors.ShowDetectionsProcessor import ShowDetectionsProcessor
from detection.ModelGenerator import ModelGenerator


execute_action = "ModelGenerator"
base_path = "C:/Alex/Dev/data_corpus/VideoCamera"


if execute_action == "ShowDetectionsProcessor":
    show_detections_processor = ShowDetectionsProcessor.load_with_custom_model(model_name="lightnings")
    show_detections_processor.show_detections([base_path + "/lightning.jpg"])

if execute_action == "VideoCameraClassImageSaverProcessor":
    video_camera_class_image_saver_processor = VideoCameraClassImageSaverProcessor.load_with_standard_model(size="m")
    video_camera_class_image_saver_processor.save_images_with_class(desired_class_name="person", show_in_screen=True)

if execute_action == "ModelGenerator":
    path_train = base_path + "/vidar.v2i.yolov8/data.yaml"
    results = ModelGenerator.train_new_model("./models/yolov8n.pt", path_train, epochs=20)
    print(results)
