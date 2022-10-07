import os
from zipfile import ZipFile


# asking user to input the ZIP file path
zip_path = input("Enter Path Of ZIP File \t")
# Resolving ZIP path
file_name = os.path.abspath(zip_path)

with ZipFile(file_name, "r") as zip:
    # printing all the contents of the zip file
    zip.printdir()
    print("Extracting ZIP files now...")

    # extracting all the files of ZIP
    zip.extractall()
    print("Extraction Done!")
