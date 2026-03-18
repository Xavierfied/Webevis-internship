from ultralytics import YOLO

WEIGHT_BB   = "Webevis-internship/video_track_yolo/weights/yolo26n.pt"
WEIGHT_POSE = "Webevis-internship/video_track_yolo/weights/yolo26n-seg.pt"



def get_stat_bb(weight=WEIGHT_BB, box=""):
    weight = YOLO(weight)
    x1, y1, x2, y2 = [int(v) for v in box.xyxy[0]]
    conf = float(box.conf[0])
    cls = int(box.cls[0])
    label = weight.names[cls]

    return x1, y1, x2, y2, conf, cls, label


def get_stat_seg(weight=WEIGHT_POSE, result="", i=""):
    weight = YOLO(weight)
    box = result.boxes[i]
    conf = float(box.conf[0])
    cls = int(box.cls[0])
    label = weight.names[cls]
    x1, y1 = int(box.xyxy[0][0]), int(box.xyxy[0][1])

    return x1, y1, conf, cls, label, box


def get_stat_pose(weight=WEIGHT_POSE, result="", i=""):
    ...