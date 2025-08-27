from detection.ModelGenerator import ModelGenerator


def exec_model_generator(train_dir, train_base_model, epochs):

    base_path = "C:/Alex/Dev/data_corpus/VideoCamera"
    path_train = base_path + "/" + train_dir + "/data.yaml"
    return ModelGenerator.train_new_model(model_path=f"./.models/{train_base_model}.pt",
                                          yaml_path=path_train,
                                          epochs=epochs)


if __name__ == '__main__':
    results = exec_model_generator(train_dir="cube.v3i.yolov8", train_base_model="yolov8m", epochs=30)
    print(results)

