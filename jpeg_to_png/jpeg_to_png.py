import sys
from PIL import Image

input_path = sys.argv[1]

try:
    Image.open(input_path).save("Converted.png")
    print("\n--------------Image Saved------------\n")
except Exception:
    print("\n--------------------File Not Found-------------------\n")
