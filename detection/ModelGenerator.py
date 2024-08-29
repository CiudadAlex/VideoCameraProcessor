from ultralytics import YOLO


class ModelGenerator:

    @staticmethod
    def train_new_model(model_path, yaml_path, epochs):

        # import torch
        # torch.cuda.set_device(0)

        # Load a model
        model = YOLO(model_path)

        # Train the model
        return model.train(data=yaml_path, epochs=epochs)

