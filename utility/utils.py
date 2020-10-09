import pyperclip
from fuzzywuzzy import process, fuzz
import random
import json
import pathlib
import shlex

directory_path = pathlib.Path(__file__).parent


def random_case(message):
    characters = []

    for character in message:
        character = random.choice([character.upper(), character.lower()])
        characters.append(character)

    return ''.join(characters)


def add(key_word, info):

    with open(directory_path/'info.json') as f:
        data = json.load(f)

    if key_word in data:
        message = (f'Are you sure you want to override {key_word} '
                   f'having value: {data[key_word]}?\t')

        if input(message) not in ('yes', 'y'):
            return
    else:
        data[key_word] = info

    with open(directory_path/'info.json', 'w') as f:
        json.dump(data, f, indent=2)


def remove(key_word):
    with open(directory_path/'info.json') as f:
        data = json.load(f)

    key = key_word

    try:
        data[key_word]
    except KeyError:
        closest_match = process.extractOne(key_word, list(data),
                                           scorer=fuzz.ratio)[0]
        if (input(f'Do you want to remove {closest_match} instead?\t')
                in ('yes', 'y')):
            key = closest_match
        else:
            return

    del data[key]

    with open(directory_path/'info.json', 'w') as f:
        json.dump(data, f, indent=2)


def list_data():
    with open(directory_path/'info.json') as f:
        data = json.load(f)

    try:
        align = max(len(key) for key in data)
    except ValueError:
        print('No data added in yet')

    for key, value in data.items():
        if len(value) > 40:
            value = f'{value[:40]}...'

        print(f'{key:{align}} - {value}')


def clipboard(key_phrase):
    with open(directory_path/'info.json') as f:
        data = json.load(f)

    best_search = process.extractOne(key_phrase, list(data),
                                     scorer=fuzz.ratio)[0]

    return data[best_search]


methods = [random_case, add, remove, list_data, clipboard]
methods = {function: function.__name__ for function in methods}


print('Available functionalities:')
for item, function in enumerate(methods.values(), start=1):
    print(f'{item}. {function}')

while True:
    command = input()

    if command.lower() == 'quit':
        break

    try:
        choice, *args = shlex.split(command)
    except ValueError:
        continue

    args = [arg if arg != '-p'
            else pyperclip.paste()for arg in args]

    try:
        function = process.extractOne(choice, methods,
                                      scorer=fuzz.ratio, score_cutoff=60)[2]
    except TypeError:
        print('Enter a valid function')
        continue

    try:
        result = function(*args)
    except TypeError:
        print('Function errored out')
        continue

    if result is not None:
        pyperclip.copy(result)
        copy_contents = pyperclip.paste()
        if len(copy_contents) > 40:
            copy_contents = f'{copy_contents[:40]}...'

        print(f'Current clipboard: {copy_contents}')
