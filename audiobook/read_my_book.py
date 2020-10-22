#!/usr/bin/python

import sys
import pyttsx3
import PyPDF2


def get_pdf(book_path):
    try:
        book = open(book_path, 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        return pdfReader
    except Exception:
        print("It doesnot look like a Pdf file. may be the path is wrong")


def text_to_speech(book_path):
    pdfReader = get_pdf(book_path)
    try:
        pages = pdfReader.numPages
        print("The Book has total: " + str(pages) + " pages!")

        # initiatiazing the pyttsx3 and setting voice speed to 125
        engine = pyttsx3.init()
        engine.setProperty('rate', 125)

        start_page = int(input("Please enter the page number: "))
        for num in range(start_page, pages):
            print("Reading page number " + str(num) + " page!")
            page = pdfReader.getPage(num)
            text = page.extractText()
            engine.say(text)
            engine.runAndWait()
            engine.stop()
    except Exception:
        print("Double check the file type or the file path")


if __name__ == "__main__":
    book_path = sys.argv[1]
    text_to_speech(book_path)
