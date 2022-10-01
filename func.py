# demo is the function name
def demo(name, age):
    # print value
    print(name, age)

# call function
demo("Ben", 25)

"""def function_name(parameter: data_type) -> return_type:
    """Doctring"""
    # body of the function
    return expression"""
#define a function with parameter
def add(num1: int, num2: int) -> int:
	"""Add two numbers"""
	num3 = num1 + num2

	return num3
# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")

"""A default argument is a parameter that assumes a default value if a value
is not provided in the function call for that argument. """
# Python program to demonstrate
# default arguments
def myFun(x, y=50):
	print("x: ", x)
	print("y: ", y)
# Driver code (We call myFun() with only
# argument)
myFun(10)
"""The idea is to allow the caller to specify the argument name with
values so that caller does not need to remember the order of parameters."""
# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
	print(firstname, lastname)

# Keyword arguments
student(firstname='Computer', lastname='Science')
student(lastname='Science', firstname='Computer')

"""In Python, we can pass a variable number of arguments to a function
using special symbols. There are two special symbols:
      *args (Non-Keyword Arguments)
    **kwargs (Keyword Arguments)"""
# Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
	for arg in argv:
		print(arg)
myFun('Hello', 'Welcome', 'to', 'Python')

# Python program to illustrate
# *kwargs for variable number of keyword arguments

def myFun(**kwargs):
	for key, value in kwargs.items():

		print("%s == %s" % (key, value))
# Driver code
myFun(first='I', mid='love', last='India')

"""The first string after the function is called the Document string or
Docstring in short. This is used to describe the functionality of the function. The use of docstring in functions is optional but it is considered a good practice.
The below syntax can be used to print out the docstring of a function:
     Syntax: print(function_name.__doc__)"""
# A simple Python function to check
# whether x is even or odd
def evenOdd(x):
	"""Function to check if the number is even or odd"""
	
	if (x % 2 == 0):
		print("even")
	else:
		print("odd")
# Driver code to call the function
print(evenOdd.__doc__)

"""A function that is defined inside another function is known as the inner
function or nested function. Nested functions are able to access variables of
the enclosing scope. Inner functions are used so that they can be protected
from everything happening outside the function."""
# Python program to
# demonstrate accessing of
# variables of nested functions
def f1():
	s = 'I love Python'
	
	def f2():
		print(s)
		
	f2()

# Driver's code
f1()

"""In Python, an anonymous function means that a function is without a name.
As we already know the def keyword is used to define the normal functions
and the lambda keyword is used to create anonymous functions.
     Syntax:
    lambda argument_list:expression"""
l = [10, 5, 12, 78, 6, 1, 7, 9]
even_nos = list(filter(lambda x: x % 2 == 0, l))
print("Even numbers are: ", even_nos)

#without lambda function
def even_numbers(nums):
    even_list = []
    for n in nums:
        if n % 2 == 0:
            even_list.append(n)
    return even_list
num_list = [10, 5, 12, 78, 6, 1, 7, 9]
ans = even_numbers(num_list)
print("Even numbers are:", ans)


"""A recursive function is a function that calls itself again and again."""

def addition(num):
    if num:
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)


"""The function return statement is used to exit from a function and
go back to the function caller and return the specified value or data item
to the caller. 
Syntax:return [expression_list]"""
def square_value(num):
	"""This function returns the square
	value of the entered number"""
	return num**2
print(square_value(2))
print(square_value(-4))

"""Local variables are those which are initialized inside a function and belong
only to that particular function. It cannot be accessed anywhere outside the function.
Let’s see how to create a local variable."""
def f():

	# local variable
	s = "I love Python"
	print(s)

# Driver code
f()
"""If we will try to use this local variable outside the function then let’s see what will happen."""

def f():
	
	# local variable
	s = "I love Python"
	print("Inside Function:", s)

# Driver code
f()
print(s)

"""These are those which are defined outside any function and which are accessible throughout
the program, i.e.,inside and outside of every function. Let’s see how to create a global variable."""
# This function uses global variable s
def f():
	print("Inside Function", s)

# Global scope
s = "I love Python"
f()
print("Outside Function", s)

"""Special Case"""
# This function has a variable with
# name same as s.


def f():
	s = "Me too."
	print(s)

# Global scope
s = "I love Python"
f()
print(s)

"""Using global keyword"""
# This function modifies the global variable 's'
def f():
	global s
	s += ' GREAT'
	print(s)
	s = "Look for Python"
	print(s)

# Global Scope
s = "Python is great!"
f()
print(s)

"""using Global and Local variable"""
a = 1

# Uses global because there is no local 'a'
def f():
	print('Inside f() : ', a)

# Variable 'a' is redefined as a local
def g():
	a = 2
	print('Inside g() : ', a)

# Uses global keyword to modify global 'a'
def h():
	global a
	a = 3
	print('Inside h() : ', a)


# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)



"""Below is the function display_student(name, age).
Assign a new name show_tudent(name, age) to it and call it using the new name."""
def display_student(name, age):
    print(name, age)

# call using original name
display_student("Emma", 26)

# assign new name
showStudent = display_student
# call using new name
showStudent("Emma", 26)






"""Note: Create a function in such a way that we can pass any number of arguments to this function,
and the function should process them and display each argument’s value."""
def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)

def calculation(a, b):
    addition = a + b
    subtraction = a - b
    # return multiple values separated by comma
    return addition, subtraction

# get result in tuple format
res = calculation(40, 10)
print(res)

# function with default argument
def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("Ben", 12000)
show_employee("Jessa")



