#!/usr/bin/python

import sys
import pyttsx3
import PyPDF2


class PdfReader:
    def __init__(self, book_path):
        self.book_path = book_path

    def get_pdf(self):
        try:
            book = open(book_path, 'rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            return pdfReader
        except Exception:
            print("It doesnot look like a Pdf file. may be the path is wrong")

    def text_to_speech(self):
        pdfReader = self.get_pdf()
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
    reader = PdfReader(book_path)
    reader.text_to_speech()
