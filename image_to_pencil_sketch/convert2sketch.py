import os
import sys
import cv2


def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)


if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        img_rgb = cv2.imread(sys.argv[1])
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        img_gray_inv = cv2.bitwise_not(img_gray)
        img_blur = cv2.GaussianBlur(img_gray_inv,
                              ksize=(21, 21), sigmaX=0, sigmaY=0)
        final_img = dodgeV2(img_gray, img_blur)
        cv2.imwrite("converted_pencil_sketch.jpg", final_img)

else:
    print("Please add a image as a argument")
