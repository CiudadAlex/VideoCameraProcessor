from detection.ModelGenerator import ModelGenerator
from processors.ShowDetectionsProcessor import ShowDetectionsProcessor
from detection.ObjectDetector import ObjectDetector


base_path = "C:/Alex/Dev/data_corpus/VideoCamera"


def exec_model_generator(train_dir, train_base_model, epochs):

    path_train = base_path + "/" + train_dir + "/data.yaml"
    return ModelGenerator.train_new_model(model_path=f"./.models/{train_base_model}.pt",
                                          yaml_path=path_train,
                                          epochs=epochs)


def exec_show_detections_processor(example_image, model_name):

    object_detector = ObjectDetector.load_custom_model(model_name=model_name)
    show_detections_processor = ShowDetectionsProcessor(object_detector)
    show_detections_processor.show_detections(list_image_path=[base_path + "/" + example_image])


if __name__ == '__main__':

    # results = exec_model_generator(train_dir="cube.v3i.yolov8",
    #                                train_base_model="yolov8m",
    #                                epochs=30)
    # print(results)

    exec_show_detections_processor(example_image="C:/Alex/Dev/docs/ArmRobot/img/photo_2025-08-08_05-46-46.jpg",
                                   model_name="cubes_size_n_30_epoch")



