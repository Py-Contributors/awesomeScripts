#!/usr/bin/env python
# python 3.8.5

import numpy
from PIL import Image


def genImage(img_width=512, img_height=256):
    # Define img width and height as an integer
    img_width = int(img_width)
    img_height = int(img_height)

    # Define key name
    filename = 'key.png'
    img_array = numpy.random.rand(img_height, img_width, 3) * 255
    '''
        Make image object from array, if u want to get
        grayscale key, use "L" on convert method.
    '''
    image = Image.fromarray(img_array.astype('uint8')).convert('RGB')

    #  Save image
    image.save(filename)
