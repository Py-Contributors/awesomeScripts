#!/usr/bin/env python3

"""
Count work frequencies within a file.
```
$ word-counter.py shakespeare.md --numWords 4 --maxTuples 3
=== Sliding Window: 1 ===
    3473: 'shall'
    2238: 'would'
    2153: 'which'
    2074: 'their'
=== Sliding Window: 2 ===
    248: 'exeunt scene'
    117: 'second lord.'
    105: 'first lord.'
    102: 'queen elizabeth.'
=== Sliding Window: 3 ===
    36: 'william shakespeare dramatis'
    34: 'shakespeare dramatis personae'
    18: 'comes here? enter'
    14: 'duke's palace enter'
```
"""

from collections import Counter
import argparse
import re
from toolz.itertoolz import sliding_window

parser = argparse.ArgumentParser()
parser.add_argument('--numWords', type=int, default=10)
parser.add_argument('--maxTuples', type=int, default=4)
parser.add_argument('--minWordLength', type=int, default=5)
parser.add_argument('file', type=str)
args = parser.parse_args()


def filter_func(tup):
    for word in tup:
        if len(word) < args.minWordLength:
            return False
        elif re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', word):
            return False
    return True


def filtered_window(seq, n):
    return filter(filter_func, sliding_window(n, seq))

with open(args.file, 'r') as f:
    content = f.read().replace('\n', ' ').lower()
    words = re.findall(r'\S+', content)
    for i in range(1, args.maxTuples + 1):
        print("\n=== Sliding Window: {} ===".format(i))
        for tup in Counter(filtered_window(words, i)).most_common(args.numWords):
            print("    {}: '{}'".format(tup[1], " ".join(tup[0])))
