from PyPDF2 import PdfFileWriter, PdfFileReader


print("The file should be in same FOLDER as this script")
pdfNameInput = input("Enter EXACT name of the PDF in this FOLDER: ")
pdfName = pdfNameInput + ".pdf"
# reading the pdf
pdf = PdfFileReader(pdfName)
# object for writing the file
write_obj = PdfFileWriter()


# Getting the number of pages and writing each page in the writer object
for i in range(pdf.getNumPages()):
    page = pdf.getPage(i)
    write_obj.addPage(page)

# Encrypting by a password
password = input("Enter Password for the Encryption to PDF: ")
write_obj.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)

new_PDF_Name_Input = input("Enter new PDF name: ")
new_PDF_Name = new_PDF_Name_Input + '.pdf'
encrypted_PDF = open(new_PDF_Name, 'wb')
write_obj.write(encrypted_PDF)
