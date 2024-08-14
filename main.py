from ObjectDetector import ObjectDetector


image_path = "C:/Alex/Dev/data_corpus/VideoCamera/person1.jpg"

objectDetector = ObjectDetector()
result = objectDetector.predict(image_path)

print("#####################################")
print(result)

