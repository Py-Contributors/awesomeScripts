#!/usr/bin/env python
# python 3.8.5

from cv2 import imread, imwrite, bitwise_xor
from generator import genImage


def xor_cipher(image, key):
    # simple xor cipher
    return bitwise_xor(image, key)


def encrypt(image):
    # generate image for the key
    genImage()
    key = imread("key.png")
    # run xor cipher to encrypt image with the key
    encrypted = xor_cipher(image, key)
    # write the image to a file
    imwrite('message_enc.png', encrypted)


def decrypt(image):
    # read the key
    key = imread("key.png")
    # run xor cipher to decrypt image with the key
    decrypted = xor_cipher(image, key)
    # write the image to a file
    imwrite('message.png', decrypted)


def main():
    # read the message
    msg_path = input(">>> Path to your image: ")
    message = imread(msg_path)

    # select mode
    mode = input(">>> Enter mode (enc: encrypt, dec: decrypt): ")
    # Conditional to check if user wants to
    # encrypt or decrypt the image
    if (mode == "enc"):
        encrypt(message)
    elif (mode == "dec"):
        decrypt(message)


if __name__ == '__main__':
    import sys
    status = main()
    sys.exit(status)
