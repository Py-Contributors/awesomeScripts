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


def get_output_dimensions(input_image, args):
    width, height = input_image.size

    if not args.Width:
        ratio = args.Height / height
        output_width = round(width * ratio)
    else:
        output_width = args.Width

    if not args.Height:
        ratio = args.Width / width
        output_height = round(height * ratio)
    else:
        output_height = args.Height

    return (output_width, output_height)


try:
    input_image = Image.open(args.File)

    width, height = get_output_dimensions(input_image, args)

    resized_image = input_image.resize((width, height))

    file_extension = os.path.splitext(args.File)[1]

    resized_image.save('output%s' % (file_extension))
except Exception as err:
    print('Could not resize image: %s' % (err))
    sys.exit(1)
