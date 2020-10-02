# Setup

Install the packages listed in `requirements.txt` using `pip`, eg: pip install pytesseract
Also, install tesseract using the steps below:

1. Install tesseract using windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki

2. Note the tesseract path from the installation.Default installation path at the time the time of this edit was: C:\Users\Program Files\Tesseract-OCR. It may change so please check the installation path.

3. pip install pytesseract

4. Change the line `pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"` to match the path of tesseract on your own pc

# Usage

Run the `imgtotxt.py` file.<br>
When you do that, you a rectangular overlay appears on your screen. Select the region of your screen that you want to convert to text.<br>
This text will be copied to your clipboard.