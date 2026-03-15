import cv2

cap = cv2.VideoCapture(0)

count = 0

while True:

    ret, frame = cap.read()

    cv2.imshow("Capture Chessboard", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):
        filename = f"calibration_images/img_{count}.jpg"
        cv2.imwrite(filename, frame)
        print("Saved:", filename)
        count += 1

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()