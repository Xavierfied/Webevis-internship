```markdown
# YOLO Object Detection Project

This repository provides a structured workflow for training and deploying YOLO models. It includes dedicated directories for dataset management, model training logs, and automated inference results.

## 📂 Project Structure

```text
yolo_train/
├── dataset/               # Training and validation data
│   ├── images/            # Source images (.jpg, .png, etc.)
│   └── labels/            # Annotation files in YOLO format (.txt)
├── exported/              # Optimized model formats (ONNX, TensorRT, etc.)
├── predictions/           # Output directory for inference results
├── runs/                  # Automatically generated training logs and weights
│   └── detect/            # Specific detection run metrics and best.pt
├── data.yaml              # Dataset configuration (paths and class names)
├── main.py                # Script to initiate model training
├── predict.py             # Script for running inference on new data
├── README.md              # Project documentation
└── yolo26n.pt             # Pre-trained or custom model weights
```

---

## 🚀 Getting Started

### 1. Installation
Clone this repository and install the required dependencies (OpenCV and Ultralytics).

```bash
pip install ultralytics opencv-python
```

### 2. Configuration
Ensure your `data.yaml` is correctly configured to point to your dataset paths.

```yaml
train: dataset/images/train
val:   dataset/images/val

nc: 2
names: ['Female', 'Male']
```

### 3. Training
Run the training script to begin fine-tuning the model on your custom dataset. Training metrics and weights will be saved to the `runs/` folder.

```bash
python main.py
```

### 4. Inference
Use the prediction script to test the model on new images. The script is configured to output results into the `predictions/` directory so make sure to manually make it before running the prediction.

```bash
python predict.py
```

---

## 🛠 Features

* **Modular Architecture:** Separates raw data from training artifacts and inference outputs for better version control.
* **Automated Results:** Inference results (like `Which_friend_are_you.png`) are automatically organized into the `predictions/` folder.
* **Ready for Export:** Includes a dedicated path for exporting `.pt` weights to edge-compatible formats like ONNX.
* **Performance Tracking:** Integrated support for monitoring mAP, precision, and recall via the `runs/` directory.

---

## 📊 Evaluation
After training, check `runs/detect/train/` for:
* `confusion_matrix.png`: To visualize classification accuracy.
* `results.png`: To view training/validation loss curves.
* `val_batch0_labels.jpg`: To verify the ground truth of your validation set.
```

Would you like me to generate a template for the `data.yaml` file or the `predict.py` script logic to go along with this?