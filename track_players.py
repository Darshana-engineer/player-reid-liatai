import cv2
import numpy as np
from ultralytics import YOLO

# Load YOLOv11 model (rename if needed)
model = YOLO("yolov11.pt")

# Load video
cap = cv2.VideoCapture("15sec_input_720p.mp4")

# Output settings
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output_with_ids.mp4", fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

# Trackers
player_id_counter = 0
player_positions = {}

def match_player(cx, cy):
    for pid, (px, py) in player_positions.items():
        if abs(px - cx) < 50 and abs(py - cy) < 50:
            return pid
    return None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame)[0]
    detections = results.boxes.xyxy.cpu().numpy()

    for det in detections:
        x1, y1, x2, y2 = map(int, det[:4])
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        matched_id = match_player(cx, cy)
        if matched_id is not None:
            player_id = matched_id
            player_positions[player_id] = (cx, cy)
        else:
            player_id_counter += 1
            player_id = player_id_counter
            player_positions[player_id] = (cx, cy)

        # Draw box and ID
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"Player {player_id}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    out.write(frame)
    cv2.imshow("Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
