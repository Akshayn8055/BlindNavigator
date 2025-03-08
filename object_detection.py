import cv2
import torch
import numpy as np
from PIL import Image

# Load YOLOv5 model using torch hub
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True).to(device)
model.eval()

def detect_objects(frame):
    """
    Runs object detection on the given frame.

    Args:
        frame (numpy.ndarray): The image frame from the Android device.

    Returns:
        list: A list of detected objects with labels and coordinates.
    """
    # Convert BGR to RGB (OpenCV loads images in BGR by default)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Convert image to PIL format (YOLOv5 expects this format)
    img_pil = Image.fromarray(rgb_frame)

    # Perform inference
    results = model(img_pil)  # No need to transform manually

    detected_objects = []

    # Process detection results
    for result in results.pandas().xyxy[0].itertuples():  # Use Pandas format
        detected_objects.append({
            "label": result.name,  # Object class
            "confidence": float(result.confidence),  # Confidence score
            "bbox": (int(result.xmin), int(result.ymin), int(result.xmax), int(result.ymax))  # Bounding box
        })

    return detected_objects
