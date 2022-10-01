"""Python too supports file handling and allows users to handle files i.e.,
to read and write files, along with many other file handling options,
to operate on files. The concept of file handling has stretched over various
other languages, but the implementation is either complicated or lengthy,
but like other concepts of Python, this concept here is also easy and short.
Python treats files differently as text or binary and this is important.
Each line of code includes a sequence of characters and they form a text file.
Each line of a file is terminated with a special character, called the EOL
or End of Line characters like comma {,} or newline character.
It ends the current line and tells the interpreter a new one has begun.
Working of open() function
Before performing any operation on the file like reading or writing, first,
we have to open that file. For this, we should use Python’s inbuilt function
open() but at the time of opening, we have to specify the mode,
which represents the purpose of the opening file.

f = open(filename, mode)
Where the following mode is supported:

r: open an existing file for a read operation.
w: open an existing file for a write operation. If the file already contains
some data then it will be overridden.
a:  open an existing file for append operation. It won’t override existing data.
r+:  To read and write data into the file. The previous data in the file will
be overridden.
w+: To write and read data. It will override existing data.
a+: To append and read data from the file. It won’t override existing data."""

# a file named "geek", will be opened with the reading mode.
file = open('abc.txt', 'r')
# This will print every line one by one in the file
for each in file:
	print (each)


"""Working of read() mode
There is more than one way to read a file in Python. If you need to extract a string that
contains all characters in the file then we can use file.read(). """
# Python code to illustrate read() mode
file = open("file.txt", "r")
print (file.read())
print (file.read(5))#read a certain number of character

"""Creating a file using write() mode
Let’s see how to create a file and how to write mode works, so in order to manipulate the file"""
# Python code to create a file
file = open('def.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()


# Python code to illustrate append() mode
file = open('geek.txt','a')
file.write("This will add this line")
file.close()

"""rstrip(): This function strips each line of a file off spaces from the right-hand side.
lstrip(): This function strips each line of a file off spaces from the left-hand side."""

# Python code to illustrate with() alongwith write()
with open("file.txt", "w") as f:
	f.write("Hello World!!!")

# Python code to illustrate split() function
with open("file.text", "r") as file:
	data = file.readlines()
	for line in data:
		word = line.split()
		print (word)


