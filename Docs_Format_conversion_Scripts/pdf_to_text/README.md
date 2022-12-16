# PDF to Text Converter

This tool will take a PDF file as input and output the text from the PDF into a text file. The PDF text is also printed in stdout.

## Requirements
-[PyPDF2](https://pypi.org/project/PyPDF2/)

## Usage

### Convert PDF to Text file
```bash
python3 pdf_to_text.py -p <PATH TO PDF> -o <PATH FOR OUTPUT TEXT>
```

e.g.
```bash
python3 pdf_to_text.py - p /home/username/Documents/sample.pdf -o /home/username/Documents/sample.txt
```
