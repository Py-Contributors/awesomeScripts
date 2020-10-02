#!/usr/bin/python
# -*- coding: utf-8 -*-
# imports section

import cv2
import os

# This text file contains the list of names of those for whom this
# certificate is being generated SEPERATED BY A NEW LINE AND NO SPACES

input_txt_file = os.path.normpath('./certificate-namelist.txt')

# This is the main certificate template image which will be used to
# generate all the certificates

template_image_path = \
    os.path.normpath('./CERTIFICATE_TEMPLATE_IMAGE.png')

# Make sure this output directory already exists

output_directory_path = os.path.dirname('./Generated_Certificates/') \
    + '/'

# Customize the font color and font size

font_size = 3.6
font_color = (51, 51, 51)

# Y adjustment determines the px to position above the horizontal
# center of the template (may be positive or negative)

coordinate_y_adjustment = -120

# X adjustment determiens the px to position to the right of verticial
# center of the template (may be positive or negative)

coordinate_x_adjustment = 7

print('Ceritificate Generation Started ...')

with open(input_txt_file) as input_list:

    content = input_list.read().splitlines()

    for line in content:

        certi_name = line

        img = cv2.imread(template_image_path)

        # Available Fonts in OpenCV:
        # Hershey Simplex: FONT_HERSHEY_SIMPLEX
        # Hershey Plain: FONT_HERSHEY_PLAIN
        # Hershey Duplex: FONT_HERSHEY_DUPLEX
        # Hershey Complex: FONT_HERSHEY_COMPLEX
        # Hershey Triplex: FONT_HERSHEY_TRIPLEX
        # Hershey Complex Small: FONT_HERSHEY_COMPLEX_SMALL
        # Hershey Script Simplex: FONT_HERSHEY_SCRIPT_SIMPLEX
        # Hershey Script Complex: FONT_HERSHEY_SCRIPT_COMPLEX

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = certi_name

        textsize = cv2.getTextSize(text, font, font_size, 10)[0]
        text_x = (img.shape[1] - textsize[0]) / 2 \
            + coordinate_x_adjustment
        text_y = (img.shape[0] + textsize[1]) / 2 \
            - coordinate_y_adjustment
        text_x = int(text_x)
        text_y = int(text_y)

        cv2.putText(
            img,
            text,
            (text_x, text_y),
            font,
            font_size,
            font_color,
            10,
        )
        certi_path = output_directory_path + certi_name + '.png'
        cv2.imwrite(certi_path, img)

cv2.destroyAllWindows()

print(
    '''Ceritificate Generation Completed.

    Find your generated certificates in ''' + output_directory_path[2::]
)
