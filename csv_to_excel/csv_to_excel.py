import openpyxl
import sys


print("This programme writes the data in any Comma-separated value file (such as: .csv or .data) to a Excel file.")
print("The input and output files must be in the same directory of the python file for the programme to work.\n")

csv_name = input("Name of the CSV file for input (with the extension): ")
sep = input("Separator of the CSV file: ")
excel_name = input("Name of the excel file for output (with the extension): ")
sheet_name = input("Name of the excel sheet for output: ")


try:
    wb = openpyxl.load_workbook(excel_name)
    sheet = wb.get_sheet_by_name(sheet_name)

    file = open(csv_name,"r",encoding = "utf-8")
except:
    print("File Error!")
    sys.exit()


row = 1
column = 1


for line in file:

    line = line[:-1]
    line = line.split(sep)


    for data in line:

        sheet.cell(row,column).value = data

        column += 1

    column = 1
    row += 1

wb.save(excel_name)
file.close()