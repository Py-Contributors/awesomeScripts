import cv2
import numpy as np
import random
import colorpicker

color = colorpicker.color()
cap = cv2.VideoCapture(0)
alive = False

point = 0
speed = 2

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))


while True:
    _, frame = cap.read()
    framecvt = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(framecvt, color[0], color[1])

    if alive is False:
        centerx = random.randint(10, 630)
        center = (centerx, 20)
        alive = True

    if(center[1] >= 450):
        alive = False
        point = 0

    centery = center[1] + speed
    center = (center[0], centery)
    zeroes = np.zeros((480, 640), dtype=np.uint8)
    zeroes[centery][center[0]] = np.uint8(1)

    mask2 = cv2.bitwise_and(mask, mask, mask=zeroes)
    points = cv2.findNonZero(mask2)
    if(points is not None):
        point = point + 1
        speed = speed + 1
        alive = False

    cv2.circle(frame, center, 5, (0, 0, 255), 10)
    cv2.putText(frame, "Points : " + str(point),
                (10, 100), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 0, 0), 1)
    out.write(frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
