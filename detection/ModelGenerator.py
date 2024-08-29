from ultralytics import YOLO


class ModelGenerator:

    @staticmethod
    def train_new_model(model_path, yaml_path):

        # Load a model
        model = YOLO(model_path)

        # Train the model
        return model.train(data=yaml_path, epochs=20)


path_train = "C:/Alex/Dev/data_corpus/VideoCamera/bird detection.v5i.yolov8/data.yaml"
results = ModelGenerator.train_new_model("yolov8n.pt", path_train)
print(results)

# FIXME pulir: train with GPU
