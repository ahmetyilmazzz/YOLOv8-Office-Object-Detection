from ultralytics import YOLO

model = YOLO('yolov8n.pt')

model.train(data='Dataset/data.yaml', epochs=15, imgsz=640)