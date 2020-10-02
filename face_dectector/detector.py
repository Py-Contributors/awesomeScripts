import cv2  # Image reading and detecting face
import argparse  # Argument Parsing

# Configuring Parser
parser = argparse.ArgumentParser()
parser.add_argument("img_path", help="Path to image")
args = parser.parse_args()


img = cv2.imread(args.img_path)  # Read Image


def detector(img):
    grey_img = cv2.cvtColor(
        img, cv2.COLOR_BGR2GRAY
    )  # Convert Color Image into Black White Image for Processing

    haar_cascades = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"  # Load Detectors
    )
    detected_img = haar_cascades.detectMultiScale(grey_img, 1.3, 5)  # Detect

    box_lst = []


    if detected_img is not None:
        for (x, y, w, h) in detected_img:
            box_lst.append([x, y, w + x, h + y])
        return box_lst  # Return Data


def draw_show(img, data):
    if data is not None:
        for face in data:
            frame = cv2.rectangle(
                img, (face[0], face[1]), (face[2], face[3]), (0, 255, 0), 2
            )

            cv2.imshow("Face Detector", frame)  # Show Processed image with bounding box
            cv2.waitKey(0)  # Wait for a key to close


print(detector(img))
draw_show(img, detector(img))
