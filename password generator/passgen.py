You can use Pythons string and random modules to generate passwords.

The string module contains a number of useful constants and classes.

Some of them we are going to use in this script.

string.ascii_letters
Concatenation of the ascii (upper and lowercase) letters

string.digits
The string ‘0123456789’.

string.punctuation
String of ASCII characters which are considered punctuation characters in the C
locale.

print string.ascii_letters

print string.digits

print string.punctuation

Output
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
!”#$%&'()*+,-./:;<=>?@[]^_`{|}~



Script -

import string
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(8, 16)))
print password
