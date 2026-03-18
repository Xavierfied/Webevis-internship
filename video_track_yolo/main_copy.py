from ultralytics import YOLO
import cv2 as cv
import numpy as np
from model.file_processor import VOD

TEST_PATH = "Webevis-internship/video_track_yolo/data/test/test.mp4"
TRAIN_PATH = "Webevis-internship/video_track_yolo/data/sample/video2.mp4"

WEIGHT =  "weights/yolo26n.pt"
WEIGHT2 =  "weights/yolo26n-seg.pt"
WEIGHT_POSE =  "Webevis-internship/video_track_yolo/weights/yolo26s-pose.pt"


################################################################################################################
################################################################################################################

class VOD:
    def __init__(self, weight, output_path, conf=0.5):
        self.weight = YOLO(weight)
        self.conf = conf
        self.output_path = output_path

################################################################################################################
    def draw_bb(self, frame, result):
        for box in result.boxes:
            x1, y1, x2, y2 = [int(v) for v in box.xyxy[0]]
            conf  = float(box.conf[0])
            cls   = int(box.cls[0])
            label = self.weight.names[cls]

            cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            text = f"{label} {conf:.2f}"
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

################################################################################################################

    def draw_seg(self, frame, result):

        if result.masks is None:
            return frame

        overlay = frame.copy()

        for i, mask_xy in enumerate(result.masks.xy):
            pts = mask_xy.astype(np.int32).reshape((-1, 1, 2))

            cv.fillPoly(overlay, [pts], color=(0, 255, 0))
            cv.polylines(frame, [pts], isClosed=True, color=(0, 255, 0), thickness=2)

            box = result.boxes[i]
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = self.weight.names[cls]

            x1, y1 = int(box.xyxy[0][0]), int(box.xyxy[0][1])

            text = f"{label} {conf:.2f}"
            cv.putText(frame, text, (x1, y1 - 5), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        cv.addWeighted(overlay, 0.4, frame, 0.6, 0, frame)

        return frame

################################################################################################################
    # def draw_pose(self, frame, result):
    #     if result.keypoints is None:
    #         return frame
    #
    #     # loop over each detected person
    #     for i, kps in enumerate(result.keypoints.xy):
    #         # kps is shape (17, 2) — 17 keypoints, each with x and y
    #         conf_scores = result.keypoints.conf[i]   # confidence per keypoint
    #
    #         # ── draw skeleton lines ─────────────────────────────────────
    #         for j, (a, b) in enumerate(SKELETON):
    #             # only draw if both keypoints were actually detected
    #             if conf_scores[a] > 0.5 and conf_scores[b] > 0.5:
    #                 x1, y1 = int(kps[a][0]), int(kps[a][1])
    #                 x2, y2 = int(kps[b][0]), int(kps[b][1])
    #
    #                 cv.line(frame, (x1, y1), (x2, y2), SKELETON_COLORS[j], 2)
################################################################################################################
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
                    verbose=False
                )

                for result in results:
                    frame = self.draw_seg(frame, result) # Change as needed

                out.write(frame)
                frame_count += 1

                # cv.imshow("VOD Tracking", frame)
                if cv.waitKey(1) & 0xFF == ord("q"):
                    break

        finally:
            cap.release()
            out.release()
            cv.destroyAllWindows()
            print(f"Output saved to: {self.output_path}")

################################################################################################################
################################################################################################################

if __name__ == "__main__":
    vod = VOD(weight=WEIGHT2, output_path="Webevis-internship/video_track_yolo/data/processed/output2.mp4", conf=0.5)
    vod.process_vid(TEST_PATH)