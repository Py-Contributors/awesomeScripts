## Html2Pdf Converter

Installation
------------

1. Install python-pdfkit:
```bash
$ pip install pdfkit  (or pip3 for python3)
```
or from `requirements.txt`
```bash
$ pip install -r requirements.txt  (or pip3 for python3)
```
2. Install wkhtmltopdf:
- Debian/Ubuntu:
```bash
$ sudo apt-get install wkhtmltopdf
```
- macOS:
```bash
$ brew install caskroom/cask/wkhtmltopdf
```

Usage
-----

For simple tasks:
```python
python html2pdf.py 'google.com' (for python3)
```
You can pass a list with multiple URLs or files:
```python
python html2pdf.py 'google.com' 'yandex.ru' 'engadget.com' (for python3)
```

Also you can pass an opened file.

Troubleshooting
---------------

- ``IOError: 'No wkhtmltopdf executable found'``:

  Make sure that you have wkhtmltopdf in your `$PATH` or set via custom configuration (see preceding section). *where wkhtmltopdf* in Windows or *which wkhtmltopdf* on Linux should return actual path to binary.

- ``IOError: 'Command Failed'``

  This error means that PDFKit was unable to process an input. You can try to directly run a command from error message and see what error caused failure (on some wkhtmltopdf versions this can be caused by segmentation faults)
