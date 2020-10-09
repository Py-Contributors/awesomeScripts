import sys
import os.path
from argparse import ArgumentParser
from PIL import Image

parser = ArgumentParser()
parser.add_argument('--file', dest='File', help='Input image filename',
                    required=True)
parser.add_argument('--width', dest='Width', help='Width in pixels',
                    type=int)
parser.add_argument('--height', dest='Height', help='Height in pixels',
                    type=int)
args = parser.parse_args()

if not args.Width and not args.Height:
    print('Error: Either width or height must be specified')
    sys.exit(1)

try:
    input_image = Image.open(args.File)
    resized_image = input_image.resize((args.Width, args.Height))
    file_extension = os.path.splitext(args.File)[1]
    resized_image.save('output.%s' % (file_extension))
except Exception:
    print('Error: Could not resize image')
    sys.exit(1)
