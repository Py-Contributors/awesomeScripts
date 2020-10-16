import cv2
import numpy as np


def extract_color(lower, upper, image):
    # do the color conversion
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower, upper)
    return mask


image = cv2.imread(r'input.jpg')
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

mask = extract_color(lower_blue, upper_blue, image)
imask = mask > 0
blue = np.zeros_like(image, np.uint8)
blue[imask] = image[imask]
cv2.imwrite("result.jpg", blue)
