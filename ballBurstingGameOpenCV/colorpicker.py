import cv2
import numpy as np


def color():
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()
        roi = frame[100:300, 0:200]
        roicvt = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        min = np.min(roicvt, axis=1)
        actualmin = np.min(min, axis=0)
        max = np.max(roicvt, axis=1)
        actualmax = np.max(max, axis=0)

        cv2.imshow('frame', roicvt)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            return[actualmin, actualmax]
            break

    cap.release()
    cv2.destroyAllWindows()
