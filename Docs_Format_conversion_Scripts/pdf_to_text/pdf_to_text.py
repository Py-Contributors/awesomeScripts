import PyPDF2
import argparse

parser = argparse.ArgumentParser(
            description = ' A program to convert PDF to Text'
                )
parser.add_argument(
        '-p',
        '--path',
        type=str,
        help='The full path of the PDf to convert',
        required = True
        )
parser.add_argument(
            '-o',
            '--output',
            type=str,
            help='Output text file name. If not specified the text will just be printed out',
            required=False
)

args = parser.parse_args()
path = args.path
text_file = args.output


#read example pdf in binary mode
pdfFileObj = open(path,'rb')

#create reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#get number of pages for the pdf
pages = pdfReader.numPages

pdfText = []
#extract text from pdf file and append it to list obj
for page_num in range(pages):
    pageObj = pdfReader.getPage(page_num)
    #text from pdf and other strings to make it look cleaner on the output
    text = pageObj.extractText() + '\n\nPage ' + str(page_num + 1) + '\n' + '*' * 80 + '\n'
    pdfText.append(text)
    print(text)
if text_file:
    #write each obj from the list to text doc    
    with open(text_file,'w', encoding="utf-8") as f:
        for page in pdfText:
            f.write(page)
#close pdf object
pdfFileObj.close()

