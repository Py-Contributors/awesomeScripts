import re
import sys


# Check if number of arguments is correct
if (len(sys.argv) < 4):
    print("Usage: python input_file.txt word_to_replace replacement")
    sys.exit(0)

# Set given arguments to variables
file_name, word1, word2 = sys.argv[1], sys.argv[2], sys.argv[3]

# Open the file and replace word1 with word2
with open(file_name, "r+") as fin:
    replaced_content = ""
    for line in fin:
        replaced_content += re.sub(word1, word2, line)

# Updates the file
with open(file_name, "w") as out:
    out.write(replaced_content)
