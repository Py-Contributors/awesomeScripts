# Program to create a basic bulk mover/copier using CLI
import os
import shutil
import argparse


# Args Function
def main():
    parser = argparse.ArgumentParser(
        prog="Muvo-CLI",
        description="Bulk move/copy files with certain extensions from all " +
        "subdirectories of a parent directory",
        epilog="Hope you found this helpful :) \n",
    )
    parser.add_argument(
        "--extensions",
        "-ext",
        nargs="+",
        required=True,
        help="List of extensions",
        type=str,
    )
    parser.add_argument(
        "--parentdir",
        "-pd",
        "--path",
        nargs="+",
        required=True,
        help="Parent directory path",
        type=str,
    )
    parser.add_argument(
        "--finaldir",
        "-fd",
        "--dest",
        nargs="+",
        required=True,
        help="Destination directory path",
        type=str,
    )
    parser.add_argument(
        "--copymove",
        "-cm",
        nargs="+",
        required=True,
        help="Copy or move files?",
        type=str,
    )
    parser.add_argument(
        "--log",
        "-l",
        nargs="+",
        required=False,
        help="Print log of files affected: yes/no",
        type=str,
    )

    args = parser.parse_args()
    # print(args.extensions[0], args.parentdir[0], args.finaldir[0],
    # args.copymove[0], args.log[0])
    mvcp(
        args.extensions,
        args.parentdir[0],
        args.finaldir[0],
        args.copymove[0],
        args.log[0],
    )


# Move/Copy Function
def mvcp(a, b, c, d, e):
    try:
        x = os.path.isdir(f"{c}")
        if x is False:
            os.mkdir(f"{c}")
        else:
            pass
        for root, dirs, files in os.walk(f"{b}"):
            for filename in files:
                name = filename.split(".")
                for extName in a:
                    if extName in name:
                        if d == "move" and not os.path.isfile(
                            f"{os.path.join(c, filename)}"
                        ):
                            shutil.move(os.path.join(root, filename), f"{c}")
                            if e == "yes" or e == "1":
                                print(os.path.join(c, filename))
                        elif d == "copy" and not os.path.isfile(
                            f"{os.path.join(c, filename)}"
                        ):
                            shutil.copy(os.path.join(root, filename), f"{c}")
                            if e == "yes" or e == "1":
                                print(os.path.join(c, filename))
                        else:
                            pass
        print("\n \nDone!")
    except shutil.Error:
        pass
    except FileNotFoundError:
        pass
    except ValueError:
        pass

    os.system("pause")


# Main Function
if __name__ == "__main__":
    print(
        "Welcome to Muvo, a small program for moving and copying" +
        " files based on extensions. You can give multiple extensions " +
        "to search for among a single directory and it'll traverse all " +
        "sub-directories and copy/move the files with the specified " +
        "extension. Enjoy! \nCredits: Navneeth M\n"
    )
    main()
