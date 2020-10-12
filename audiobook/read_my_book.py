import pyttsx3
import PyPDF2
book = open('sample.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

print("The Book has total: " + str(pages) + " pages!")

start_page = 0
speaker = pyttsx3.init()
for num in range(start_page, pages):
    print("Reading page number " + str(num) + " page!")
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
