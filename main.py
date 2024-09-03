from processors.VideoCameraClassImageSaverProcessor import VideoCameraClassImageSaverProcessor
from processors.VideoCameraClassVideoSaverProcessor import VideoCameraClassVideoSaverProcessor
from processors.ShowDetectionsProcessor import ShowDetectionsProcessor
from detection.ModelGenerator import ModelGenerator
from utils.Log import Log


if __name__ == '__main__':
    Log.config()

    execute_action = "ShowDetectionsProcessor_BIRDS"
    base_path = "C:/Alex/Dev/data_corpus/VideoCamera"

    if execute_action == "ShowDetectionsProcessor_LIGHTNINGS":
        show_detections_processor = ShowDetectionsProcessor.load_with_custom_model(model_name="lightnings")
        show_detections_processor.show_detections(list_image_path=[base_path + "/lightning.jpg"])

    if execute_action == "ShowDetectionsProcessor_BIRDS":
        show_detections_processor = ShowDetectionsProcessor.load_with_custom_model(model_name="birds_gpu_40_epoch")
        show_detections_processor.show_detections(list_image_path=[base_path + "/birds.jpg"])

    if execute_action == "VideoCameraClassImageSaverProcessor_BIRDS":
        video_camera_class_image_saver_processor = VideoCameraClassImageSaverProcessor.load_with_custom_model(model_name="birds")
        video_camera_class_image_saver_processor.save_images_with_class(desired_class_name="bird", show_in_screen=True)

    if execute_action == "VideoCameraClassImageSaverProcessor_LIGHTNINGS":
        video_camera_class_image_saver_processor = VideoCameraClassImageSaverProcessor.load_with_custom_model(model_name="lightnings")
        video_camera_class_image_saver_processor.save_images_with_class(desired_class_name="Lightning", show_in_screen=True)

    if execute_action == "VideoCameraClassVideoSaverProcessor_PERSONS":
        video_camera_class_video_saver_processor = VideoCameraClassVideoSaverProcessor.load_with_standard_model(size="n")
        video_camera_class_video_saver_processor.save_videos_with_class(desired_class_name="person", show_in_screen=False)

    if execute_action == "VideoCameraClassVideoSaverProcessor_BIRDS":
        video_camera_class_video_saver_processor = VideoCameraClassVideoSaverProcessor.load_with_custom_model(model_name="birds")
        video_camera_class_video_saver_processor.save_videos_with_class(desired_class_name="bird", show_in_screen=True)

    if execute_action == "VideoCameraClassVideoSaverProcessor_LIGHTNINGS":
        video_camera_class_video_saver_processor = VideoCameraClassVideoSaverProcessor.load_with_custom_model(model_name="lightnings")
        video_camera_class_video_saver_processor.save_videos_with_class(desired_class_name="Lightning", show_in_screen=False)

    if execute_action == "ModelGenerator_BIRDS":
        path_train = base_path + "/bird detection.v5i.yolov8/data.yaml"
        results = ModelGenerator.train_new_model(model_path="./.models/yolov8n.pt", yaml_path=path_train, epochs=50)
        print(results)

    if execute_action == "ModelGenerator_LIGHTNINGS":
        path_train = base_path + "/vidar.v2i.yolov8/data.yaml"
        results = ModelGenerator.train_new_model(model_path="./.models/yolov8n.pt", yaml_path=path_train, epochs=50)
        print(results)


# FIXME check
'''

import ffmpeg

packet_size = 4096

process = ffmpeg.input('rtsp://deuterio:D3uT33RR10@192.168.0.21:554/stream1').output('./.out/audio.mp4', format='mulaw').run_async(pipe_stdout=True)
packet = process.stdout.read(packet_size)

while process.poll() is None:
    packet = process.stdout.read(packet_size)
    print(packet)
'''