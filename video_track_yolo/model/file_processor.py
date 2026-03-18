from ultralytics import YOLO
import cv2 as cv
import numpy as np

from utils.frame_stat    import get_stat_bb
from utils.obj_detector  import draw_bb
from utils.segmenter     import draw_seg
from utils.pose_profiler import draw_pose

################################################################################################################

class VOD:
    def __init__(self, weight, output_path, conf=0.5):
        self.weight = YOLO(weight)
        self.conf = conf
        self.output_path = output_path
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
#
# if __name__ == "__main__":
#     vod = VOD(weight=WEIGHT2, output_path="Webevis-internship/video_track_yolo/data/processed/output2.mp4", conf=0.5)
#     vod.process_vid(TEST_PATH)