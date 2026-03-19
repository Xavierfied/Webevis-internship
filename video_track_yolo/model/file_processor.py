from ultralytics import YOLO
import cv2 as cv
import numpy as np

from utils.obj_detector  import draw_bb
from utils.segmenter     import draw_seg
from utils.pose_profiler import draw_pose
from utils.frame_stat import vid_stat

MODES = {
    "detection":    draw_bb,
    "segmentation": draw_seg,
    "pose":         draw_pose
}

################################################################################################################

class VOD:
    def __init__(self, weight, output_path, conf=0.29, mode="detection"):
        if mode not in MODES:
            raise ValueError(f"Invalid mode '{mode}'. Choose from: {list(MODES.keys())}")

        self.weight = YOLO(weight)
        self.conf = conf
        self.output_path = output_path
        self.draw_fn = MODES[mode]
    ################################################################################################################
    def process_vid(self, input_path):
        cap, width, height, fps, fourcc, out = vid_stat(input_path, self.output_path)

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
                    frame = self.draw_fn(frame, result, self.weight) # Change as needed

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
