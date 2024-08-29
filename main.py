from detection.ObjectDetector import ObjectDetector
from processors.ClassImageSaverProcessor import ClassImageSaverProcessor

base_path = "C:/Alex/Dev/data_corpus/VideoCamera"


def test_bird():
    object_detector = ObjectDetector.load_custom_model(model_name="birds")
    image_path = base_path + "/birds.jpg"
    results = object_detector.predict(image_path)
    ObjectDetector.show_results(results)


# test_bird()


class_image_saver_processor = ClassImageSaverProcessor.load_with_standard_model(size="m")
class_image_saver_processor.save_images_with_class(desired_class_name="person", show_in_screen=False)

