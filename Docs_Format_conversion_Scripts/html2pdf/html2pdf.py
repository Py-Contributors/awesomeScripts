#!/usr/bin/python
# -*- coding: utf-8 -*-
# a Python script to generate pdf from URL

import pdfkit
import sys


def converttopdf(url):
    pdfkit.from_url(url, 'out.pdf')


if __name__ == '__main__':
    converttopdf(str(sys.argv[1:]))
