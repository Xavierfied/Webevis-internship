import os
import gdown
from model.file_processor import VOD

################################################################################################################

TEST_PATH  = "data/test/test.mp4"
TRAIN_PATH = "data/sample/video2.mp4"

WEIGHTS = {
    "detection":    "weights/yolo26n.pt",
    "segmentation": "weights/yolo26n-seg.pt",
    "pose":         "weights/yolo26s-pose.pt"
}

DRIVE_IDS = {
    "detection":    "https://drive.google.com/file/d/1c4JfOZCgMKypjk5T7rZYDdhwEEKzhW-e/view?usp=sharing",
    "segmentation": "https://drive.google.com/file/d/1tzVzzU9Fj9iiR1FNX7ih7Qwud8lWIIqy/view?usp=drive_link",
    "pose":         "your_google_drive_id_here"
}

################################################################################################################

def fetch_weight(mode):
    path = WEIGHTS[mode]

    if not os.path.exists(path):
        print(f"[INFO] Weight not found at '{path}', downloading from Google Drive...")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        gdown.download(url=DRIVE_IDS[mode], output=path, quiet=False)
        print(f"[INFO] Downloaded to '{path}'")
    else:
        print(f"[INFO] Weight found at '{path}'")

    return path

################################################################################################################

if __name__ == "__main__":

    MODE   = "detection"   # change to "detection" or "pose" as needed
    OUTPUT = f"data/processed/output_{MODE}.mp4"

    weight = fetch_weight(MODE)

    vod = VOD(weight=weight, output_path=OUTPUT, conf=0.5, mode=MODE)
    vod.process_vid(TEST_PATH)