"""Python Random module is an in-built module of Python which is used to
generate random numbers. These are pseudo-random numbers means these are not
truly random. This module can be used to perform random actions such as
generating random numbers,print random a value for a list or string, etc."""
# import random
import random

# prints a random value from the list
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))

import random
random.seed(5)
print(random.random())
print(random.random())


"""random.randint() method is used to generate random
integers between the given range.
Syntax :
randint(start, end)"""
# Python3 program explaining work
# of randint() function
# import random module
import random
# Generates a random number between
# a given positive range
r1 = random.randint(5, 15)
print("Random number between 5 and 15 is % s" % (r1))
# Generates a random number between
# two given negative range
r2 = random.randint(-10, -2)
print("Random number between -10 and -2 is % d" % (r2))

"""random.random() method is used to generate random floats between 0.0 to 1.
Syntax: 
random.random()"""

# Python3 program to demonstrate
# the use of random() function .
	
# import random
from random import random
	
# Prints random item
print(random())

"""random.choice() function is used to return a random item from a list, tuple, or string.
Syntax:
random.choice(sequence)"""

# Python3 program to demonstrate the use of
# choice() method

# import random
import random

# prints a random value from the list
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))

# prints a random item from the string
string = "python"
print(random.choice(string))

# prints a random item from the tuple
tuple1 = (1, 2, 3, 4, 5)
print(random.choice(tuple1))

"""random.shuffle() method is used to shuffle a sequence (list). Shuffling means changing
the position of the elements of the sequence. Here, the shuffling operation is inplace.

Syntax:
random.shuffle(sequence, function)"""
# import the random module
import random


# declare a list
sample_list = [1, 2, 3, 4, 5]

print("Original list : ")
print(sample_list)

# first shuffle
random.shuffle(sample_list)
print("\nAfter the first shuffle : ")
print(sample_list)

# second shuffle
random.shuffle(sample_list)
print("\nAfter the second shuffle : ")
print(sample_list)

