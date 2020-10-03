from PyPDF2 import PdfFileMerger

print("\nMake sure you have copied two pdfs \
            in the same FOLDER as this script :) \n")

input("\nPress ENTER to begin the SCRIPT !!!\n")

firstPdf = input("\nEnter the EXACT NAME of your first PDF: \n") + ".pdf"

secondPdf = input("\nEnter the PATH of your second PDF:\n") + ".pdf"

result = input("\nEnter the final name of the Merged PDF: \n") + ".pdf"

pdfs = [firstPdf, secondPdf]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write(result)
merger.close()

print(
    "\nYour PDF has been merged :)\n \
     Thank You for using this Script :D Cheers !!! \n"
)
