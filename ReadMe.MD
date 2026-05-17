# 🚗 Smart Parking Detection using YOLO

Detect empty and occupied parking spaces in real time using a custom-trained YOLOv8 model and a Streamlit web interface.

---

## Features

- **Image Upload** — Upload a parking lot photo and instantly detect empty/occupied slots
- **Live Camera** — Stream from a webcam with real-time detection and slot counting
- **Confidence Threshold** — Adjustable slider to control detection sensitivity
- **Slot Counter** — Displays total empty 🟢 and occupied 🔴 spaces after each inference

---

## Project Structure

```
Smart-Parking-Yolo/
├── dataset/
│   └── data.yaml          # YOLO dataset config
├── model/
│   └── best.pt            # Trained YOLO model weights
├── runs/                  # Training output (auto-generated)
├── training/
│   └── train.py           # Model training script
├── app/
│   └── stramlit_app.py             # Streamlit web app
└── README.md
```

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/Smart-Parking-Yolo.git
cd Smart-Parking-Yolo
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install ultralytics streamlit opencv-python pillow
```

---

## Training

To train the model on your own dataset:

```bash
python training/train.py
```

Training config (in `train.py`):

| Parameter | Value |
|-----------|-------|
| Model     | YOLOv8n (nano) |
| Epochs    | 50 |
| Image Size | 640 |
| Batch Size | 4 |

After training, copy the best weights to `model/best.pt`:

```bash
cp runs/parking_yolo_demo/weights/best.pt model/best.pt
```

---

## Running the App

```bash
streamlit run app/stramlit_app.py 
```

Then open your browser at `http://localhost:8501`.

---

## Dataset Format

The dataset follows standard YOLO format with two classes:

```yaml
# data.yaml
names:
  0: empty
  1: occupied
```

---

## Requirements

- Python 3.8+
- ultralytics
- streamlit
- opencv-python
- pillow