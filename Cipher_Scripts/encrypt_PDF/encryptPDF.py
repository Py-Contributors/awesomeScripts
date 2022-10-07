import os
import argparse
from PyPDF2 import PdfFileWriter, PdfFileReader

arg = argparse.ArgumentParser()
arg.add_argument("-f", "--file", required=True, help="Path to PDF file")
arg.add_argument("-p", "--password", required=True, help="Password to encrypt PDF file")
args = vars(arg.parse_args())


def encryptPDF(pdf_path, password):
    """ 
    function to encrpyt a PDF file using PyPDF2
    
    Args:
        pdfName (str): path to PDF file
        password (str): password to encrypt PDF file
    
    Returns:
        None
    """
    pdf = PdfFileReader(pdf_path)
    # object for writing the file
    write_obj = PdfFileWriter()


    # Getting the number of pages and writing each page in the writer object
    for i in range(pdf.getNumPages()):
        page = pdf.getPage(i)
        write_obj.addPage(page)

    # Encrypting by a password
    write_obj.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)

    new_PDF_Name = os.path.basename(pdf_path).split(".")[0] + "_encrypted.pdf"
    encrypted_PDF = open(new_PDF_Name, 'wb')
    write_obj.write(encrypted_PDF)

if __name__ == "__main__":
    pdf_path =  args["file"]
    password = args["password"]
    encryptPDF(pdf_path, password)
    
