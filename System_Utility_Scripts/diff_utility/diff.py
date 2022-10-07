#!/usr/bin/env python3

# sys: for reading command-line arguments.
# rich: for coloring the text.
import sys
from rich import print

# Print Usage message if enough arguments are not passed.
if len(sys.argv) < 3:
    print("Usage:")
    print("\tMust provide two file names as command-line arguments.")
    print("\tdiff.py <orignal_file> <changed_file>")
    exit(1)

orignal = sys.argv[1]
changed = sys.argv[2]

cr = "bold red"
cg = "bold green"

# Read the contents of the files in lists.
orignal_contents = open(orignal, "r").readlines()
changed_contents = open(changed, "r").readlines()

co = "green"
sy = f"[bold {co}][+]"

print()

# Determine which file has changed much.
if len(changed_contents) <= len(orignal_contents):
    co = "red"
    sy = f"[bold {co}][-]"
    smallest_sloc, largest_sloc = changed_contents, orignal_contents
else:
    smallest_sloc, largest_sloc = orignal_contents, changed_contents

# Go over all the lines to check the changes.
for line in range(0, len(smallest_sloc)):
    if orignal_contents[line] == changed_contents[line]:
        # Ignore if the lines are same.
        continue
    else:
        # Display the changes on the respective lines of the files.
        oc = orignal_contents[line]
        cc = changed_contents[line]
        print(f"[{cr}][-] Line {line + 1}:[{cr}] {oc}", end="")
        print(f"[{cg}][+] Line {line + 1}:[{cg}] {cc}")

        # Show the additions or deletions for the file that is the largest.
        if line == len(smallest_sloc) - 1:
            for new_line in range(line + 1, len(largest_sloc)):
                ls = largest_sloc[new_line]
                print(f"{sy} Line {new_line + 1}:[bold {co}] {ls}")
