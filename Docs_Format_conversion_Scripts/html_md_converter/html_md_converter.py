import argparse
import os

import html2md
import mistune
from bs4 import BeautifulSoup as bs


def md_to_html(input_, output):
    md = open(input_, 'r').read()

    html = "<!DOCTYPE html><html><head></head><body>"
    html += mistune.markdown(md, escape=False)
    html += "</body></html>"

    soup = bs(html, "html.parser")
    prettyHTML = soup.prettify()

    with open(output, "w") as mrd:
        mrd.write(prettyHTML)


def html_to_md(input_, output):
    html = open(input_, "r").read()
    md = html2md.convert(html)

    with open(output, "w") as mrd:
        mrd.write(md)


def main():
    # Collect arguments
    parser = argparse.ArgumentParser(
        description="Convert Markdown File to HTML file"
    )
    parser.add_argument('input', help='file you want to convert')

    args = parser.parse_args()
    filename, ext = os.path.splitext(args.input)

    if ext == ".html":
        output = filename + ".md"
        html_to_md(args.input, output)
    elif ext == ".md":
        output = filename + ".html"
        md_to_html(args.input, output)
    else:
        raise ValueError('Invalid file type')


if __name__ == "__main__":
    main()
