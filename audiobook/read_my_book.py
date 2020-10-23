#!/usr/bin/python

import pyttsx3
import PyPDF2


class AudioBook:
    def __init__(self, book_path):
        self.book_path = book_path

    def text_to_speech(self):
        with open(self.book_path, "rb") as book:
            pdfReader = PyPDF2.PdfFileReader(book)
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
