import sys
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
