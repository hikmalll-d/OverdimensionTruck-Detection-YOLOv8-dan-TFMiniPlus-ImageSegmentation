import cv2
import numpy as np
import serial
from ultralytics import YOLO

camera_matrix = np.load("camera_matrix.npy")
dist_coeff = np.load("dist_coeff.npy")

model = YOLO("best.pt")

ser = serial.Serial('COM3',115200)

def read_distance():
    try:
        data = ser.readline().decode().strip()
        return float(data)
    except:
        return 0

def get_scale(distance):
    return 0.105 * distance - 0.01

cap = cv2.VideoCapture(0)

HEIGHT_LIMIT = 120

while True:

    ret, frame = cap.read()

    frame = cv2.undistort(frame, camera_matrix, dist_coeff)

    results = model(frame)

    distance = read_distance()

    for r in results:

        boxes = r.boxes

        for box in boxes:

            x1,y1,x2,y2 = map(int, box.xyxy[0])

            pixel_height = y2 - y1

            scale = get_scale(distance)

            real_height = pixel_height * scale

            if real_height > HEIGHT_LIMIT:
                status = "OVER DIMENSION"
                color = (0,0,255)
            else:
                status = "NORMAL"
                color = (0,255,0)

            cv2.rectangle(frame,(x1,y1),(x2,y2),color,2)

            text = f"{real_height:.1f} cm | {status}"

            cv2.putText(frame,
                        text,
                        (x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        color,
                        2)

    cv2.putText(frame,
                f"Distance: {distance:.2f} m",
                (20,40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255,255,255),
                2)

    cv2.imshow("ODOL Detection", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()