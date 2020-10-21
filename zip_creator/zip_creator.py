import os
from zipfile import ZipFile

# asking user to input the directory path
dir_path = input("Enter Path Of Directory \t")

# resolving directory and zip file name based on OS of the user
dir_name = os.path.abspath(dir_path)
zip_name = os.path.basename(os.path.normpath(dir_path)) + ".zip"


# function to zip the directory
def zipdir(dir_path, zip):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            zip.write(os.path.join(root, file))


# main function
if __name__ == "__main__":
    zipfile = ZipFile(zip_name, "w")

    # calling zipdir function
    zipdir(dir_name, zipfile)
    zipfile.close()
    print("Zipping Success!")
