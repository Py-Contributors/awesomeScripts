import sys

# Taking the filename from system arguments
filename = sys.argv[1]

def word_counter():
    frequency = {}

    # Opening the file
    with open(filename) as file:
        # Reading each line of file using readlines()
        for line in file.readlines():
            # Splitting lines into words using line.split()
            for word in line.split():
                # Checking if there are any numbers or symbols in the text.
                # Considering words which contains only alphabets
                if word.isalpha():
                    # Checking if word is present in dictionary or not.
                    # If not present we add it to the frequency dictionary,
                    # otherwise we increase its occurrence by 1.
                    if frequency.get(word.lower()) is None:
                        frequency[word.lower()] = 1
                    else:
                        frequency[word.lower()] += 1

    # Sorting the dictionary using sorted() and lambda functions.
    # Here lambda function is used to sort dictionary by values i.e sorting words by their frequency
    words = sorted(frequency.items(), key = lambda word : word[1], reverse = True)

    print("\nWords stored in file, ranked according to frequency are :\n\n")
    for word in words:
        print(word[0])

if __name__ == "__main__":
    word_counter()
