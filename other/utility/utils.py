"""This script has a bunch of utility functions.

All commands are issued from stdin, however, this behaves a lot like
a command line script. If any argument needs multiple words, enclose
them in double-quotes `"`

"""

import datetime
import functools
import json
import pathlib
import random
import shlex
import subprocess
import time
from typing import Callable, Mapping, TypeVar

import dateparser
import humanize
import pyperclip
from fuzzywuzzy import fuzz, process

directory = pathlib.Path(__file__).parent
json_file = directory / 'info.json'
ding = directory / 'ding.mp3'

RT = TypeVar('RT')


def read(function: Callable[..., RT]) -> Callable[..., RT]:
    """Take in a function, open the json file and pass in its data to
       the function.

    Parameters
    ----------
    function : Callable
        Should have a positional argument at the start to which the
        data will be passed

    Returns
    -------
    Callable
        The wrapper function which does the execution
    """
    @functools.wraps(function)
    def reader(*args) -> RT:

        with open(json_file) as f:
            data = json.load(f)

        return function(data, *args)
    return reader


def write(function: Callable[..., Mapping[str, str]]) -> Callable[..., None]:
    """Take in a function, store it's result and write it to the JSON

    Parameters
    ----------
    function : Callable
        Should return a valid dictionary which can be written to the
        JSON file

    Returns
    -------
    Callable
        The wrapper function which does the execution
    """
    @functools.wraps(function)
    def writer(*args) -> None:

        data = function(*args)

        with open(json_file, 'w') as wf:
            json.dump(data, wf, indent=2)

    return writer


def copy_to_clipboard(function: Callable[..., str]) -> Callable[..., None]:
    """Take in a function, store its result, copy it to the clipboard
       and display it.

    Parameters
    ----------
    function : Callable
        The function should return the string which is to be copied
        to the clipboard.

    Returns
    -------
    Callable
        The wrapper function which does the execution.
    """
    @functools.wraps(function)
    def copy(*args) -> None:

        result = function(*args)
        pyperclip.copy(result)

        if len(result) > 40:
            result = f'{result[:40]}...'

        print(f'Current clipboard: {result}')

    return copy


@copy_to_clipboard
def random_case(message: str) -> str:
    """Convert the string to RanDoM CasE.

    Parameters
    ----------
    message : str
        The string to be converted

    Returns
    -------
    str
        The string in RandOm caSe
    """
    characters = []

    for character in message:
        converted_char = random.choice([character.upper(), character.lower()])
        characters.append(converted_char)

    return ''.join(characters)


@write
@read
def add(data: dict[str, str], key_word: str, info: str) -> dict[str, str]:
    """Add provided key and value to the JSON file.

    Parameters
    ----------
    data : dict of str, str
        Internally used by `read` to pass in the current data
    key_word : str
        The key to be used
    info : str
        The value to be stored in the key

    Returns
    -------
    dict of str, str
        Internally used by the `write` decorator to update the current
        data.

    Raises
    ------
    Exception
        When the user doesn't want to override the value stored in the
        `keyword` when it already exists.
    """

    if key_word in data:
        message = (f'Are you sure you want to override {key_word} '
                   f'having value: {data[key_word]}?\t')
        if input(message) not in ('yes', 'y'):
            raise Exception('Exited')

    data[key_word] = info
    return data


@write
@read
def remove(data: dict[str, str], key_word: str) -> dict[str, str]:
    """Remove `key_word` from the JSON file.

    Parameters
    ----------
    data : dict of str, str
        Internally passed in by `read` to provide the current data
        in the file
    key_word : str
        The key to be removed

    Returns
    -------
    dict of str, str
        The updated data with the key removed

    Raises
    ------
    Exception
        When the user doesn't want to remove the recommended
        fuzzy-matched string incase `key_word` doesn't already
        exist
    """

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
            raise Exception('Exited')

    del data[key]
    return data


@read
def list_data(data: dict[str, str]) -> None:
    """Print the current data in the JSON file in a pretty format.

    Parameters
    ----------
    data : dict of str, str
        Internally passed in by `read` to provide the current data
        in the file
    """
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
def clipboard(data: dict[str, str], key_phrase: str) -> str:
    """Copy the value stored in the passed in key

    Parameters
    ----------
    data : dict of str, str
        Internally passed in by `read` to provide the current data
        in the file
    key_phrase : str
        The key to copy the value of

    Returns
    -------
    str
        The value in the key
    """
    best_search = process.extractOne(key_phrase, list(data),
                                     scorer=fuzz.ratio)[0]

    return data[best_search]


def diceroll(num_faces: str = "6") -> None:
    """Roll a dice and print the result

    Parameters
    ----------
    num_faces : str, optional
        The faces of the die, by default 6
    """
    print(random.randint(1, int(num_faces)))


def timer(sleep_for: str) -> None:
    """A snazzy timer

    It prints the time left into the console, and plays a sound when
    completed.

    Parameters
    ----------
    sleep_for : str
        The duration the timer to run for, in any valid format.
        The format could be a human readable one or a stricter
        one.

    Raises
    ------
    ValueError
        If the format provided is invalid or the sleep duration
        is negative
    """

    current = datetime.datetime.now()
    sleep_date = dateparser.parse(sleep_for, languages=['en'])

    if sleep_date is None:
        raise ValueError('Time not recognised')

    sleep_seconds = round((current - sleep_date).total_seconds())

    if sleep_seconds < 0:
        raise ValueError("sleep period must be positive")

    while sleep_seconds:
        print('\r' + ' ' * 100, end='\r\t')
        print(humanize.naturaltime(sleep_seconds, future=True), end='\r')

        time.sleep(1)
        sleep_seconds -= 1
    else:
        print()

    subprocess.run(['open', ding])


methods = {function: function.__name__ for function in [
    random_case, add, remove, list_data, clipboard, diceroll, timer
]}


print('Available functionalities:')
for item, function in enumerate(methods.values(), start=1):
    print(f'{item}. {function}')
else:
    print()

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
    finally:
        print()
