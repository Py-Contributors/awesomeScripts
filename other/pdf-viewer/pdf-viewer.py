# Building a basic PDF Viewer using python

# importing all things from tkinter

from tkinter import *
from tkinter import filedialog
import PyPDF2

# creating the root rootdow 
root= Tk()
root.geometry("800x600")
root.title("Your PDF Viewer")
root.config(bg="GREY")

# Creating the Text Box
text_box = Text(root,width= 80,height=60)
text_box.pack(pady=15)

# Function to open the pdf file
def open_pdf():
   file= filedialog.askopenfilename(title="Select a PDF File", filetype=(("PDF    Files","*.pdf"),("All Files","*.*")))
   if file:
      #Open the PDF File
      pdf_file= PyPDF2.PdfFileReader(file)
      #Select a Page to read
      page= pdf_file.getPage(0)
      #Get the content of the Page
      content=page.extractText()
      #Add the content to TextBox
      text_box.insert(1.0,content)

# Function to clear the text 
def clear_text():
   text_box.delete(1.0, END)

# Function to Quit the rootdow
def quit_app():
   root.destroy()

# Creating different options 
options= Menu(root)
root.config(menu=options)

file_menu=Menu(options,tearoff=False)


text_box.config(bg="BLACK", fg="WHITE")
options.add_cascade(label="Open a File",command=open_pdf)
options.add_cascade(label="Clear Text",command=clear_text)
options.add_cascade(label="Quit",command=quit_app)
 
root.mainloop()