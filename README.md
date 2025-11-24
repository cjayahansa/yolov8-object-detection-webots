# YOLOv8 Dog Detection Robot in Webots

## Overview
This project is created for **learning purposes**.  
It uses **YOLOv8** to detect a **dog** in real-time using a robot in **Webots**.  
The robot's camera captures frames, YOLOv8 detects the dog, and the robot moves toward it.  
The detection is also displayed in an **OpenCV window**.

---

## Features
- Real-time dog detection with YOLOv8
- Robot follows the detected dog
- Camera feed displayed with bounding boxes
- Beginner-friendly project to learn **OpenCV**, **YOLO**, and **robot control**

---

## Requirements
- Python 3.8+
- Webots Simulator
- Ultralytics YOLOv8 (`pip install ultralytics`)
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)

---

## How to Run
1. Open your robot world in Webots.  
2. Run the controller script:
```bash
python camera_controller_yolov8n.py
```
![image](https://github.com/cjayahansa/yolov8-object-detection-webots/blob/main/Screenshot%20from%202025-11-25%2000-58-24.png)
![image](https://github.com/cjayahansa/yolov8-object-detection-webots/blob/main/Screenshot%20from%202025-11-25%2000-59-34.png)
![image](https://github.com/cjayahansa/yolov8-object-detection-webots/blob/main/Screenshot%20from%202025-11-25%2001-10-37.png)

