from detection.ObjectDetector import ObjectDetector
from rtsp_client.RtspClient import RtspClient
import time

base_path = "C:/Alex/Dev/data_corpus/VideoCamera"


def predict(obj_detector, image_name):

    print("#####################################")
    results = obj_detector.predict(base_path + "/" + image_name)

    for r in results:

        r.show()  # Display the image with predictions
        #r.save()  # Save the image with predictions
        '''
        boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # convert to int values

            confidence = math.ceil((box.conf[0] * 100)) / 100

            # class name
            cls = int(box.cls[0])

            print(f"Class name: {r.names[cls]}. Confidence: {confidence}. Window ---> (x1, y1) = ({x1}, {y1}), (x2, y2) = ({x2}, {y2})")
'''


def predict_batch():

    object_detector = ObjectDetector(size="x")

    predict(object_detector, "person1.jpg")
    predict(object_detector, "cat_dog.jpg")
    predict(object_detector, "bus1.jpg")


def test_cam():
    rtsp_client = RtspClient.from_config_file('config.properties')

    for i in range(10):
        time.sleep(2.5)
        rtsp_client.show_screen()

    rtsp_client.close()


# predict_batch()
test_cam()

