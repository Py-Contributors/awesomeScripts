import json
import argparse
import difflib as dif

'''
    Simple English Dictionary c:

'''


def dic(word):
    # if the word is written correctly
    if word in data:
        return data[word]

    close_match = dif.get_close_matches(word, data.keys())
    if not close_match:
        return 'Unknown word. Please, try again'
    else:
        close_match = close_match[0]
    # if the similarity to another word is greater than 0.6
    if dif.SequenceMatcher(None, word, close_match).ratio() > 0.6:
        # asks if the other word is the right word
        answer = input(f'Did you mean {close_match}? Y or N\n')
        answer = answer.upper()
        if answer == 'Y':
            # if was the right one, returns the meaning
            return data[close_match]
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

    word = args.word
    out = dic(word)

    if isinstance(out, list):
        # checks if out is a list of meanings to show line by line
        for x in range(len(out)):
            print(f"{x + 1} - " + out[x])
    else:
        print(out)
