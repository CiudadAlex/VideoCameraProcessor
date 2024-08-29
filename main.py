from processors.VideoCameraClassImageSaverProcessor import VideoCameraClassImageSaverProcessor
from processors.ShowDetectionsProcessor import ShowDetectionsProcessor


base_path = "C:/Alex/Dev/data_corpus/VideoCamera"


show_detections_processor = ShowDetectionsProcessor.load_with_custom_model(model_name="birds")
show_detections_processor.show_detections([base_path + "/birds.jpg"])

'''
video_camera_class_image_saver_processor = VideoCameraClassImageSaverProcessor.load_with_standard_model(size="m")
video_camera_class_image_saver_processor.save_images_with_class(desired_class_name="person", show_in_screen=False)
'''
