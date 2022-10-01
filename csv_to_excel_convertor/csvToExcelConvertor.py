import csv
from openpyxl import Workbook


def convertCsvToXlsx(self):
    wb = Workbook()
    sheet = wb.active

    CSV_SEPARATOR = ","

    with open("file.csv") as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                for idx, val in enumerate(col.split(CSV_SEPARATOR)):
                    cell = sheet.cell(row=r + 1, column=idx + 1)
                    cell.value = val

    wb.save("convertedFile.xlsx")


if __name__ == '__main__':
    convertCsvToXlsx()
