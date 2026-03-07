from ultralytics import YOLO
import cv2 as cv

TEST_PATH = "Webevis-internship/video_track_yolo/data/test/test.mp4"
TRAIN_PATH = "Webevis-internship/video_track_yolo/data/sample/video2.mp4"

WEIGHT =  "weights/yolo26n.pt"
#
# model = WEIGHT
#
# results = model.track(source=TRAIN_PATH, show=True, conf=0.1)
# cv.waitKey(0)


class VOD:
    def __init__(self, weight, video_path, output_path, conf=0.5):
        self.weight = YOLO(weight)
        self.cap = cv.VideoCapture(video_path)
        self.conf = conf

        width = int(self.cap.get(cv.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        fps = int(self.cap.get(cv.CAP_PROP_FPS))
        fourcc = cv.VideoWriter.fourcc(*"mpv4")

        self.out = cv.VideoWriter(output_path, fourcc, fps, (width, height))


    def draw_boxes(self):

        pass