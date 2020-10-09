import json
import argparse
import difflib as dif

'''
    Simple English Dictionary c:

'''

def dic(word):
    if word in data:
        return data[word]   # if the word is written correctly
    elif dif.SequenceMatcher(None, word, dif.get_close_matches(word, data.keys())[0]).ratio() > 0.6:  # if the similarity to another word is greater than 0.6
        answer = input('Did you mean {}? Y or N\n'.format(dif.get_close_matches(word, data.keys())[0]))  # asks if the other word is the right word
        answer = answer.upper()
        if answer == 'Y':
            return data[dif.get_close_matches(word, data.keys())[0]]  # if was the right one, returns the meaning
        elif answer == 'N':
            return 'Unknown word. Please, try again'
        else:
            return 'Unknown command. Please, try again'
    else:
        return 'Unknown word. Please, try again'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='English Dictionary')
    parser.add_argument('word', help='Input word to search')
    args = parser.parse_args()

    data = json.load(open('data.json'))  # loads the dictionary

    while True:
        word = args.word
        out = dic(word)

        if isinstance(out, list):  # checks if out is a list of meanings to show line by line
            for x in range(len(out)):
                print(f"{x + 1} - " + out[x])
            break
        else:
            print(out)
            break
