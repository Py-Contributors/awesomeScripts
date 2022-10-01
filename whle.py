"""The while loop in Python is used to iterate over a block of code as long as the test
expression (condition) is true.
  We generally use this loop when we don't know beforehand, the number of times to iterate.
  In while loop, test expression is checked first. The body of the loop is entered only if the
test_expression evaluates to True. After one iteration, the test expression is checked again.
This process continues until the test_expression evaluates to False.
  In Python, the body of the while loop is determined through indentation.
Body starts with indentation and the first unindented line marks the end.
Python interprets any non-zero value as True. None and 0 are interpreted as False."""

#syntax
"""statement x
while(condition):
       statement block
statement y"""

# Program to add natural
# numbers upto 
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)

print()
#2
i=0
while(i<=10):
    print(i,end=" ")
    i+=1

print()

#3 
i=0
print('with tab')
while(i<=100):
    print(i,end='\t')
    i+=1

"""Python’s print() function comes with a parameter called ‘end’. By default, the value of this
parameter is ‘\n’, i.e. the new line character.
You can end a print statement with any character/string using this parameter."""



