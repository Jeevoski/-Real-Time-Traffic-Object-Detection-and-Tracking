import cv2
import numpy as np
from ultralytics import YOLO
from sort import Sort

# Load YOLOv8 model
model = YOLO('yolov8n.pt')  # Use 'yolov8s.pt' for better accuracy

# Load video
cap = cv2.VideoCapture("traffic_video.mp4")  # Replace with your video
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)

# Show info
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = frame_count / fps
print(f"Video duration: {duration:.2f} sec, FPS: {fps}, Total frames: {frame_count}")

# Initialize SORT tracker
tracker = Sort()

# COCO class names
class_names = [
    "person", "bicycle", "car", "motorcycle", "airplane", "bus", "train",
    "truck", "boat", "traffic light", "fire hydrant", "stop sign", "parking meter",
    "bench", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear",
    "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase",
    "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
    "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle",
    "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
    "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut",
    "cake", "chair", "couch", "potted plant", "bed", "dining table", "toilet",
    "tv", "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave",
    "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase",
    "scissors", "teddy bear", "hair drier", "toothbrush"
]

# Only track these classes
target_classes = [0, 2, 3, 5, 7]  # person, car, motorcycle, bus, truck

# Count setup
line_position = 300
counted_ids = set()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(frame, verbose=False)[0]

    detections = []
    class_map = {}

    for i, box in enumerate(results.boxes):
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        if cls_id in target_classes and conf > 0.3:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            detections.append([x1, y1, x2, y2, conf])

    detections_np = np.array(detections)
    tracks = tracker.update(detections_np)

    for det, track in zip(detections, tracks):
        track_id = int(track[4])
        det_index = detections.index(det)
        cls_id = int(results.boxes.cls[det_index])
        class_map[track_id] = class_names[cls_id]

    for track in tracks:
        x1, y1, x2, y2, track_id = map(int, track)
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        label = f"{class_map.get(track_id, 'object')} ID {track_id}"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
        cv2.circle(frame, (cx, cy), 3, (0, 0, 255), -1)

        # Count crossing the line
        if line_position - 5 < cy < line_position + 5 and track_id not in counted_ids:
            counted_ids.add(track_id)

    # Draw counting line
    cv2.line(frame, (0, line_position), (frame.shape[1], line_position), (255, 0, 0), 2)
    cv2.putText(frame, f"Count: {len(counted_ids)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Traffic Detection", frame)
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

