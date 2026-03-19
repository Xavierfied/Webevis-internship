from ultralytics import YOLO
import cv2 as cv



def vid_stat(video_path, output_path):
    capt = cv.VideoCapture(video_path)

    if not capt.isOpened():
        raise ValueError(f"Cannot open video: {video_path}")

    width = int(capt.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(capt.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps = int(capt.get(cv.CAP_PROP_FPS))
    fourcc = cv.VideoWriter.fourcc(*"mp4v")
    out = cv.VideoWriter(output_path, fourcc, fps, (width, height))

    return capt, width, height, fps, fourcc, out



def get_stat_bb(weight, box):

    x1, y1, x2, y2 = [int(v) for v in box.xyxy[0]]
    conf = float(box.conf[0])
    cls = int(box.cls[0])
    label = weight.names[cls]

    return x1, y1, x2, y2, conf, cls, label


def get_stat_seg(weight, result, i):

    box = result.boxes[i]
    conf = float(box.conf[0])
    cls = int(box.cls[0])
    label = weight.names[cls]
    x1, y1 = int(box.xyxy[0][0]), int(box.xyxy[0][1])

    return x1, y1, conf, cls, label, box


# def get_stat_pose(model, result, i):
#     box = result.boxes[i]
#     conf = float(box.conf[0])
#     cls = int(box.cls[0])
#     label = model.names[cls]
#     x1, y1 = int(box.xyxy[0][0]), int(box.xyxy[0][1])
#     x2, y2 = int(box.xyxy[0][2]), int(box.xyxy[0][3])
#     kps = result.keypoints.xy[i]
#     conf_scores = result.keypoints.conf[i]
#
#     return x1, y1, x2, y2, conf, label, kps, conf_scores