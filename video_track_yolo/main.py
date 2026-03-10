from sympy.codegen.ast import none
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
    def __init__(self, weight, output_path, conf=0.5):
        self.weight = YOLO(weight)
        self.conf = conf
        self.output_path = output_path


    def vid_stat(self, video_path):
        capt = cv.VideoCapture(video_path)

        if not capt.isOpened():
            raise ValueError(f"Cannot open video: {video_path}")

        width   = int(self.capt.get(cv.CAP_PROP_FRAME_WIDTH))
        height  = int(self.capt.get(cv.CAP_PROP_FRAME_HEIGHT))
        fps     = int(self.capt.get(cv.CAP_PROP_FPS))
        fourcc = cv.VideoWriter.fourcc(*"mpv4")
        out = cv.VideoWriter(self.output_path, fourcc, fps, (width, height))

        return capt, width, height, fps, fourcc, out


    def draw_bb(self, frame, result):
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf  = float(box.conf[0])
            cls   = int(box.cls[0])
            label = self.weight.names[cls]

            cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            text       = f"{label} {conf:.2f}"
            (tw, th), _ = cv.getTextSize(text, cv.FONT_HERSHEY_SIMPLEX, 0.6, 2)
            cv.rectangle(frame, (x1, y1 - th - 8), (x1 + tw, y1), (0, 255, 0), -1)

            cv.putText(
                frame, text,
                (x1, y1 - 4),
                cv.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 0, 0), 2
            )

            if box.id is not None:
                track_id = int(box.id[0])
                cv.putText(
                    frame, f"ID:{track_id}",
                    (x1, y2 + 20),
                    cv.FONT_HERSHEY_SIMPLEX,
                    0.55, (255, 100, 0), 2
                )

        return frame


    def process_vid(self, input_path):
        cap, width, height, fps, fourcc, out = self.vid_stat(input_path)

        frame_count = 0

        try:
            while True:
                ret, frame = cap.read()

                if not ret:
                    print(f"Finished — {frame_count} frames processed.")
                    break

                results = self.weight.track(
                    frame,
                    conf=self.conf,
                    persist=True,
                )

                for result in results:
                    frame = self.draw_bb(frame, result)

                out.write(frame)
                frame_count += 1

                cv.imshow("VOD Tracking", frame)
                if cv.waitKey(1) :
                    break

        finally:
            cap.release()
            out.release()
            cv.destroyAllWindows()
            print(f"Output saved to: {self.output_path}")


if __name__ == "__main__":
    vod = VOD(weight=WEIGHT, output_path="output.mp4", conf=0.4)
    vod.process_vid(TRAIN_PATH)