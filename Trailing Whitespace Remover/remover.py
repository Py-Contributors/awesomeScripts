import argparse

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
for fname in args.files:
    lines = [i.rstrip() for i in open(fname, "r").readlines()]
    with open(fname, "w"):
        pass
    with open(fname, "w") as f:
        f.write("\n".join(lines))
