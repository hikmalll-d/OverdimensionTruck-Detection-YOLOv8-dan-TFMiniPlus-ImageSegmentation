import cv2
import numpy as np

camera_matrix = np.load("camera_matrix.npy")
dist_coeff = np.load("dist_coeff.npy")

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    undistorted = cv2.undistort(frame, camera_matrix, dist_coeff)

    cv2.imshow("Original", frame)
    cv2.imshow("Undistorted", undistorted)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()