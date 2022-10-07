import urllib.request
import string

dictionary = (
    "https://raw.githubusercontent.com/dwyl/ \
    english-words/master/words_alpha.txt"
)

alphabet = {letter: 0 for letter in string.ascii_lowercase}
total_amount = 0

with urllib.request.urlopen(dictionary) as req:
    for line in req:
        dec_line = line.decode("UTF-8").strip().lower()
        for letter in dec_line:
            alphabet[letter] += 1

        total_amount += len(line)

for letter in alphabet:
    print(
        f"{letter.upper()}:\t{alphabet[letter]}\
         t{round(alphabet[letter]/total_amount*100, 2)}%"
    )

print("--------------------------")
print(f"Total amount: {total_amount}")
