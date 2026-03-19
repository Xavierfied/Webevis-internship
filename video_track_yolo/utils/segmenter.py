import numpy as np
import cv2 as cv
from .frame_stat import get_stat_seg


def draw_seg(frame, result, weight):
    if result.masks is None:
        return frame

    overlay = frame.copy()

    for i, mask_xy in enumerate(result.masks.xy):
        pts = mask_xy.astype(np.int32).reshape((-1, 1, 2))

        cv.fillPoly(overlay, [pts], color=(0, 255, 0))
        cv.polylines(frame, [pts], isClosed=True, color=(0, 255, 0), thickness=2)

        x1, y1, conf, cls, label, box = get_stat_seg(weight, result, i)  # ← pass model

        text = f"{label} {conf:.2f}"
        cv.putText(frame, text,
                   (x1, y1 - 5),
                   cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv.addWeighted(overlay, 0.4, frame, 0.6, 0, frame)

    return frame