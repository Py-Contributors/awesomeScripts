# Program to create a basic bulk mover/copier
import os
import shutil

print(
    "Welcome to Muvo, a small program for moving and copying files based on" +
    " extensions. You can give multiple extensions to search for among a " +
    "single directory and it'll traverse all sub-directories and copy/move " +
    "the files with the specified extension. Enjoy! \nCredits: Navneeth M\n"
)


# Main function
def mvcp():
    ext = input(
        "Enter a single line of the extension(s) you want to search for " +
        "separated by spaces: "
    ).split(" ")
    path = input(
        'Enter a parent directory path without " " ' +
        '(The directory HAS to exist): '
    )
    dest = input('Enter a final directory path without " " : ')
    cmconsent = int(input("Do you want to\n1. Copy Files\n2. Move Files "))
    true = input(
        "Do you want to the see the names of the files moved: " +
        "\n1. yes \n2. no "
    )
    x = os.path.isdir(f"{dest}")
    if x is False:
        os.mkdirs(f"{dest}")
    else:
        pass
    for root, dirs, files in os.walk(f"{path}"):
        for filename in files:
            name = filename.split(".")
            for extName in ext:
                if extName in name:
                    if cmconsent == 2 and os.path.isfile(
                        f"{os.path.join(dest, filename)}"
                    ) is False:
                        shutil.move(os.path.join(root, filename), f"{dest}")
                        if true == "yes" or true == "1":
                            print(os.path.join(dest, filename))
                    elif cmconsent == 1 and os.path.isfile(
                        f"{os.path.join(dest, filename)}"
                    ) is False:
                        shutil.copy(os.path.join(root, filename), f"{dest}")
                        if true == "yes" or true == "1":
                            print(os.path.join(dest, filename))
                    else:
                        pass
    print("\n \nDone!")


# Error Blocks
try:
    mvcp()
except shutil.Error:
    pass
except FileNotFoundError:
    pass
except ValueError:
    pass

while True:
    ch = input("Do you want to transfer/copy files again? (y/n)")
    if ch.lower() == "y":
        try:
            mvcp()
        except shutil.Error:
            pass
    elif ch.lower() == "n":
        break

os.system("pause")
