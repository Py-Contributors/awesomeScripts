""" Script to find duplicate files in a given path """
import os
import hashlib

from sys import argv

# will store file realted info
# structure: keys => file size
# values = a dict(), structure: keys => is_duplicate, filepath, sha1, sha256
files = {}

# will store duplicate files
# structure: keys => filepath of parent file in group of duplicates
# values = a list of filepath of duplicates
dups = {}

stats = {
    "total_files": 0,
    "current_file": 0,
    "duplicates": 0,
    "size": 0
}


def progress():
    print(
        """\r[{0}/{1}] files checked ||  \b[{2}/{3}] duplicates found.""".
        format(
            stats["current_file"],
            stats["total_files"],
            stats["duplicates"],
            stats["current_file"]
        ), end="")


def load(path):
    path = os.walk(path)

    for dirpath, dirnames, filenames in path:
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)

            # skips symbolic link
            if not os.path.islink(filepath):
                key = os.path.getsize(filepath)
                if key not in files:
                    files[key] = []

                stats["total_files"] += 1
                print(f"\rFiles Traversed: {stats['total_files']}", end="")
                files[key].append({
                    "is_duplicate": False,
                    "filepath": filepath,
                })


def add_sha1(file_info):
    BUF_SIZE = 1024
    sha1 = hashlib.sha1()
    with open(file_info["filepath"], 'rb') as file:
        data = file.read(BUF_SIZE)
        sha1.update(data)
    file_info["sha1"] = sha1.hexdigest()


def is_equal_sha1(file1_info, file2_info):
    add_sha1(file1_info)
    add_sha1(file2_info)
    return file1_info["sha1"] == file2_info["sha1"]


def add_sha256(file_info):
    BUF_SIZE = 65536
    sha256 = hashlib.sha256()
    with open(file_info["filepath"], 'rb') as file:
        while True:
            data = file.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)
    file_info["sha256"] = sha256.hexdigest()


def is_equal_sha256(file1_info, file2_info):
    if "sha256" not in file1_info:
        add_sha256(file1_info)
    if "sha256" not in file2_info:
        add_sha256(file2_info)
    return file1_info["sha256"] == file2_info["sha256"]


def find():
    for key in files:

        # pick file from a group
        for idx, file1_info in enumerate(files[key]):

            # skip if already in list of duplicates
            if file1_info["is_duplicate"]:
                continue

            # compare picked file with file to the right
            for ptr in range(idx + 1, len(files[key])):
                file2_info = files[key][ptr]

                # skip if already in list of duplicates
                if file2_info["is_duplicate"]:
                    continue

                if is_equal_sha1(file1_info, file2_info):
                    if is_equal_sha256(file1_info, file2_info):
                        file2_info["is_duplicate"] = True

                        stats["duplicates"] += 1
                        stats["size"] += key

                        if file1_info["filepath"] not in dups:
                            dups[file1_info["filepath"]] = []
                        dups[file1_info["filepath"]].append(
                            file2_info["filepath"])

        # update progress
        stats["current_file"] += len(files[key])
        progress()


def store():
    with open("duplicates.txt", "w") as file:
        for key in dups:
            file.write(f"Duplicate of {key} is at:\n")
            for entry in dups[key]:
                file.write(entry + "\n")
            file.write("\n\n")


def print_stats():
    print("\n\nTotal no of duplicates:", stats["duplicates"])

    KB = 1024
    MB = 1024 * 1024
    GB = 1024 * 1024 * 1024

    dupsSize = stats["size"]
    if dupsSize >= GB:
        print("Total space taken by duplicates: %.02lf GB" %
              (dupsSize / GB))
    elif dupsSize >= MB:
        print("Total space taken by duplicates: %.02lf MB" %
              (dupsSize / MB))
    elif dupsSize >= KB:
        print("Total space taken by duplicates: %.02lf KB" %
              (dupsSize / KB))
    else:
        print(f"Total space taken by duplicates: {dupsSize} Bytes")


def main():
    # Validate command line args
    if not len(argv) > 1:
        print("Usage: python dupsfinder.py <path>")
        return
    start_path = argv[1]

    # traverse file tree and group files on the basis of there size
    load(start_path)

    # find duplicates
    find()

    # writes duplicates in a file
    store()

    print_stats()


if __name__ == "__main__":
    main()
