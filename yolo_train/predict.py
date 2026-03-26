from ultralytics import YOLO
import cv2
from pathlib import Path

MODEL_PATH  = "model/best.pt"
INPUT       = "Which_friend_are_you.png"
OUTPUT_DIR  = "predictions/"
CONFIDENCE  = 0.1

Path(OUTPUT_DIR).mkdir(exist_ok=True)

model = YOLO(MODEL_PATH)
results = model.predict(source=INPUT, conf=CONFIDENCE, device=0)

for result in results:
    img_path = Path(result.path).name
    annotated = result.plot()
    cv2.imwrite(f"{OUTPUT_DIR}/{img_path}", annotated)
    print(f"✅ Saved: {OUTPUT_DIR}/{img_path}")

print(f"\nDone! All predictions saved to '{OUTPUT_DIR}'")