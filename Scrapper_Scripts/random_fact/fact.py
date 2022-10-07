"""Gets a random fact and displays it.

Script usage:
    $ python3 -m fact.py [type]

    type can be one of the following: math, trivia, date, year, if not
    specified, a random fact type will be chosen.

Module usage:
    >>> import fact
    >>> fact.get_random_fact('math')
    '2913 is a value of n for which s(n-1) + s(n+1) = s(2n).'
"""

import requests


def get_random_fact(topic: str) -> str:
    """Get a random fact of the supplied topic from NumbersAPI

    Requirements:
        Access to the API is neccessary although a key is not required.

    :param topic: The topic for the fact
    :type topic: str
    :returns: A fact as a standalone sentence.
    :rtype: str
    """

    url = f"http://numbersapi.com/random/{topic}"

    res = requests.get(url)
    res.raise_for_status()

    return res.text


def _main() -> None:
    """Helper function for script execution

    :rtype: None
    """

    import random
    import sys

    try:
        topic = sys.argv[1]
    except IndexError:
        topic = random.choice(('math', 'trivia', 'date', 'year'))

    fact = get_random_fact(topic)

    print(f"Random '{topic}' fact!\n{fact}")


if __name__ == "__main__":
    _main()
