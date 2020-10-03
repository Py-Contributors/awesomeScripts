# Title :- Trailing Whitespace Remover

# Importing Argument Parser
import argparse

# Creating Argument Parser
parser = argparse.ArgumentParser(
    description="Remove Trailing Whitespaces from files."
)

parser.add_argument(
    "files",
    type=str,
    nargs="+",
    help="Files to remove trailing whitespace from."
)

args = parser.parse_args()
for fname in args.files:  # iterating over each file provided
    # remove trailing characters from each line
    lines = [i.rstrip() for i in open(fname, "r").readlines()]
    with open(fname, "w"):
        pass  # truncate to remove text from file
    with open(fname, "w") as f:
        f.write("\n".join(lines))  # write new clean text
