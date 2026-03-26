import os
import shutil
import random
from pathlib import Path
from ultralytics import YOLO
######################################################################################################
BASE_DIR     = Path(__file__).parent.resolve()  
EXPORTED_DIR = BASE_DIR / "exported"
DATASET_DIR  = BASE_DIR / "dataset"
SPLIT_RATIO  = 0.8
CLASSES      = ["Male", "Female"]

######################################################################################################

def prepare_dataset():
    src_images = Path(EXPORTED_DIR) / "images"
    src_labels = Path(EXPORTED_DIR) / "labels"

    for split in ["train", "val"]:
        (Path(DATASET_DIR) / "images" / split).mkdir(parents=True, exist_ok=True)
        (Path(DATASET_DIR) / "labels" / split).mkdir(parents=True, exist_ok=True)

    image_files = [
        f for f in src_images.iterdir()
        if f.suffix.lower() in [".jpg", ".jpeg", ".png"]
        and (src_labels / f.with_suffix(".txt").name).exists()
    ]

    random.seed(42)
    random.shuffle(image_files)

    split_idx  = int(len(image_files) * SPLIT_RATIO)
    train_files = image_files[:split_idx]
    val_files   = image_files[split_idx:]

    def copy_files(files, split):
        for img_path in files:
            lbl_path = src_labels / img_path.with_suffix(".txt").name
            shutil.copy(img_path, Path(DATASET_DIR) / "images" / split / img_path.name)
            shutil.copy(lbl_path, Path(DATASET_DIR) / "labels" / split / lbl_path.name)

    copy_files(train_files, "train")
    copy_files(val_files,   "val")

    print(f" Dataset ready — Train: {len(train_files)} | Val: {len(val_files)}")




def train():
    model = YOLO("yolo26n.pt")
    model.train(
        data="data.yaml",
        epochs=50,
        imgsz=640,
        batch=8,
        name="male_female_detector",
        device=0
    )
    print("Training complete — best weights at: runs/detect/male_female_detector/weights/best.pt")

######################################################################################################    

if __name__ == "__main__":
    # prepare_dataset()
    train()
