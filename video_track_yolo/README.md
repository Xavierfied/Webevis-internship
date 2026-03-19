# Video Object Detection (VOD) — YOLOv8 Tracker

Real-time video object detection and tracking using YOLOv8 and OpenCV.

---

## Project Structure

```
video_track_yolo/
├── data/
│   ├── processed/
│   │   ├── output.mp4
│   │   └── output2.mp4
│   ├── sample/
│   │   └── video2.mp4
│   └── test/
├── weights/
│   └── yolo26n.pt
├── main.py
├── README.md
└── requirements.txt
```

---

## Requirements

```
ultralytics
opencv-python
```

Install with:

```bash
pip install ultralytics opencv-python
```

## Run Script

Change your Directory to "video_track_yolo" with following command:
```
cd video_track_yolo
```
Then run the following command:
```
python main.py
```
## Change Mode
Change the Tracking Mode you desire by changing the input in "main.py" Line:41, You may select between the following:
```
detection
segmentation
```