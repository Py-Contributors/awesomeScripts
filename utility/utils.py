import datetime
import functools
import json
import pathlib
import random
import shlex
import subprocess
import time

import dateparser
import pyperclip
from fuzzywuzzy import fuzz, process

directory = pathlib.Path(__file__).parent
json_file = directory/'info.json'
ding = directory/'ding.mp3'


def read(function):
    @functools.wraps(function)
    def reader(*args):

        with open(json_file) as f:
            data = json.load(f)

        return function(data, *args)
    return reader


def write(function):
    @functools.wraps(function)
    def writer(*args):

        data = function(*args)

        with open(json_file, 'w') as wf:
            json.dump(data, wf, indent=2)

    return writer


def copy_to_clipboard(function):
    @functools.wraps(function)
    def copy(*args):

        result = function(*args)
        pyperclip.copy(result)

        if len(result) > 40:
            result = f'{result[:40]}...'

        print(f'Current clipboard: {result}')

    return copy


@copy_to_clipboard
def random_case(message):
    characters = []

    for character in message:
        character = random.choice([character.upper(), character.lower()])
        characters.append(character)

    return ''.join(characters)


@write
@read
def add(data, key_word, info):

    if key_word in data:
        message = (f'Are you sure you want to override {key_word} '
                   f'having value: {data[key_word]}?\t')
        if input(message) not in ('yes', 'y'):
            return data

    data[key_word] = info
    return data


@write
@read
def remove(data, key_word):
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
            return data

    del data[key]
    return data


@read
def list_data(data):
    try:
        align = max(len(key) for key in data)
    except ValueError:
        print('No data added in yet')
        return

    for key, value in data.items():
        if len(value) > 40:
            value = f'{value[:40]}...'

        print(f'{key:{align}} - {value}')


@copy_to_clipboard
@read
def clipboard(data, key_phrase):

    best_search = process.extractOne(key_phrase, list(data),
                                     scorer=fuzz.ratio)[0]

    return data[best_search]


def diceroll(num_faces=6):
    print(random.randint(1, int(num_faces)))


def timer(sleep_for):
    current = datetime.datetime.now()
    sleep_date = dateparser.parse(sleep_for, languages=['en'])

    if sleep_date is None:
        raise ValueError('Time not recognised')

    sleep_seconds = round((current - sleep_date).total_seconds())

    if sleep_seconds < 0:
        raise ValueError("sleep period must be positive")

    while sleep_seconds:
        print(f'\t{sleep_seconds} seconds(s) remaining', end='\r')
        time.sleep(1)
        sleep_seconds -= 1
    else:
        print(' ' * 30, end='\r')

    subprocess.Popen(['open', ding])


methods = [random_case, add, remove, list_data, clipboard, diceroll, timer]
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
            else pyperclip.paste() for arg in args]

    try:
        function = process.extractOne(choice, methods,
                                      scorer=fuzz.ratio, score_cutoff=60)[2]
    except TypeError:
        print('Enter a valid function')
        continue

    try:
        function(*args)
    except Exception as e:
        print('Function errored out')
        print(e)
