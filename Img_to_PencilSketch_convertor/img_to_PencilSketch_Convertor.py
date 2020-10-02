import cv2
import sys
filename = 'Enter Your File path' # Eg: E:/Friends_family/IMG-20190406-WA0023.jpg
image = cv2.imread(filename)
#Check if the Input Image Exists or Not
if image is None:
    print("No Image Found! Enter Proper Image Path!")
    sys.exit()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Image Inversion on Grayscale
inverted_images = 255 - gray_image
inverted_images = cv2.GaussianBlur(inverted_images, (21, 21), 0)
output = cv2.divide(gray_image, 255-inverted_images, scale=256.0)
cv2.namedWindow("Input_Image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Pencil_Sketch", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Input_Image", image)
cv2.imshow("Pencil_Sketch", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
