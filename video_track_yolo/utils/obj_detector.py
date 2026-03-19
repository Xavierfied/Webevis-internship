import cv2 as cv
from .frame_stat import get_stat_bb


def draw_bb(frame, result, weight):
    for box in result.boxes:


        x1, y1, x2, y2, conf, cls, label = get_stat_bb(box=box, weight=weight)

        cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        text = f"{label} {conf:.2f}"
        (tw, th), _ = cv.getTextSize(text, cv.FONT_HERSHEY_SIMPLEX, 0.6, 2)

        cv.rectangle(frame, (x1, y1 - th - 8), (x1 + tw, y1), (0, 255, 0), -1)
        cv.putText(frame, text,
                   (x1, y1 - 4),
                   cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

        if box.id is not None:
            track_id = int(box.id[0])
            cv.putText(
                frame, f"ID:{track_id}",
                (x1, y2 + 20),
                cv.FONT_HERSHEY_SIMPLEX,
                0.55, (255, 100, 0), 2
            )

    return frame