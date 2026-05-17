from ultralytics import YOLO
import os

project_root = r"D:\project-computerVision\Smart-Parking-Yolo"

data_yaml = os.path.join(project_root, "dataset", "data.yaml")

model = YOLO("yolov8n.pt")

model.train(
    data=data_yaml,
    epochs=50,
    imgsz=640,
    batch=4,
    name="parking_yolo_demo",
    project=os.path.join(project_root, "runs")
)

print("Training finished successfully!")