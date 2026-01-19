# YOLOv8 Office Object Detection

This project uses YOLOv8 to detect objects in an office environment.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ahmetyilmazzz/YOLOv8-Office-Object-Detection.git
   cd YOLOv8-Office-Object-Detection
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the pre-trained model:
   The model `yolov8n.pt` is not included in the repository due to its size. You can download it from the official YOLOv8 repository or by running the following command:
   ```bash
   wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt
   ```

## Usage

To run the object detection on an image, use the following command:
```bash
python main.py
```
