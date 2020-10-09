import sys
import os.path
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--file', dest='File', help='Input image filename')
parser.add_argument('--width', dest='Width', help='Width in pixels')
parser.add_argument('--height', dest='Height', help='Height in pixels')
parser.add_argument('--output', dest='Output', default='output',
                    help='The output folder')
args = parser.parse_args()

if not args.Width and not args.Height:
    print('Error: Either width or height must be specified')
    sys.exit(1)

if args.File and not os.path.isfile(args.File):
    print('Error: The specified file does not exist')
    sys.exit(1)
