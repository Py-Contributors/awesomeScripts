import sys
from PIL import Image

input_path = sys.argv[1]

Image.open(input_path).save("Converted.png")
print("Image Saved")
