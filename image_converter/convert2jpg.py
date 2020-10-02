import os
import sys
from PIL import Image

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        im = Image.open(sys.argv[1]).convert("RGBA")
        target_name = sys.argv[1].split(".")[0] + ".jpg"
        background = Image.new("RGBA", im.size, (255, 255, 255))
        alpha_composite = Image.alpha_composite(background, im)
        alpha_composite.convert("RGB").save(target_name, "JPEG", quality=100)
        print("Saved as " + target_name)
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: convert2jpg.py <file>")
