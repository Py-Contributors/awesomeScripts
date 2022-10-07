import sys
import os
import subprocess


def epub_to_awz3(file_path):
    """
    Convert An Ebook To Kindle Format.
    """
    if file_path.split(".")[-1] == "epub":
        if os.path.isfile(file_path):
            output_path = get_output_path(file_path)
            try:
                subprocess.call(["ebook-convert", file_path, output_path])
            except Exception as e:
                print(e)
        else:
            print("Bad File Path!")
    else:
        print("Bad File Extension!")


def get_output_path(file_path):
    """
    Helper Function That Returns Output Filepath At
    The Same Location Of Source With Changed Extension
    """
    output_path = file_path.split(".")
    output_path[-1] = ".azw3"
    return "".join(output_path)


if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except Exception as e:
        print(e)
        print("Please Enter The Ebook File Path as a Command-Line Argument!")
        exit(0)
    epub_to_awz3(file_path)
    print("Succesfully Converted!")
