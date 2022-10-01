#concat
str1="SOUVIK "
str2="MAJUMDAR"
str3=str1+str2
print(str3)
print()
 
#appending
str1="HELLO "
str2="Souvik"
str1+=str2
str1+="!Welcome to python..."
print(str1)
print()
 
#Reapeating
str="RCCIIT"
print(str*3)
print()
 
#reference checking
str1="SOUVIK"
print("First String ID is : ",id(str1))
str2="MAJUMDAR"
print("Second String ID is : ",id(str2))
print()
 
#reference checking
str1="SOUVIK"
print("First String ID is : ",id(str1))
str2="SOUVIK"
print("Second String ID is : ",id(str2))
print()
 
#Immutability
str1="SOUVIK"
print("Before Concatenating : ",id(str1))
str2="MAJUMDAR"
str1+=str2
print("After Concatenating  : ",id(str2))
print(str1)
print()
 
#Foramtting
name = "RCCIIT"
age=21
print("Name = %s and Age = %d"%(name,age))
print("Name = %s and Age = %d"%("HJCHDGD",175))
print()
 
#Stripping
str="awedaewdawefawsdewa"
print(str.strip('awd'))
print()
 
#Slicing with positive Index
str="PYTHON"
print("str[0:4] = ",str[0:4])
print("str[:6] = ",str[:6])
print("str[1:] = ",str[1:])
print("str[:] = ",str[:])
print("str[0:20] = ",str[0:20])
print()
 
#slicing with negetive index
str="PYTHON"
print("str[-1] = ",str[-1])
print("str[:-4] = ",str[:-4])
print("str[-2:] = ",str[-2:])
print("str[-3:-1] = ",str[-3:-1])
print()
 
#slicing with stride
str="SCALASPARK"
print("str[2:10] = ",str[2:10])
print("str[2:10:1] = ",str[2:10:1])
print("str[2:10:2] = ",str[2:10:2])
print("str[2:10:4] = ",str[2:10:4])
 
#splice with positive
str="Welcome to Python "
print("str[::3] = ",str[::3])
print()
 
#splice with negetive
str="Welcome to Python "
print("str[::-1] = ",str[::-1])
print("str[::-3] = ",str[::-3])
print()
 
 
#ord() and #chr()
print(ord('R'))
print(chr(113))
print()
 
#in operator
str1="Welcome to the Python"
str2=" the"
if str2 in str1:
    print("Found")
else:
    print("Not Found")
print()
 
#not in operator
str3="OTT is the best platform for the box office "
str4="best"
if str4 not in str3:
    print("Present")
else:
    print("Not Present")
print()
 
#comparing operators are ==(equal) != or <>(not equal)
 
#uses character to iterate
new_str=''
str=input("\nEnter a String : \n")
for i in str:
    new_str+=i
print("\nThe copied string using character  is  : ",new_str)
 
#uses index of character to iterate
new_str2=''
str=input("\nEnter a String :\n")
for i in range(len(str)):
    new_str2+=str[i]
print("\nThe Copied string using index is : ",new_str2)
print()
 
#string index must be integer
str="PYTHON"
print(str)
print(str[4])
print(str['Y'])
print()



#different methods on string object 
import string
 
 
str="Welcome to World of Python"
print("UpperCase ",str.upper())
print("LowerCase ",str.lower())
print("Split ",str.split())
print("Join ",str.join(str.split()))
print("Replace ",str.replace("Python","Java"))
print("Count of o ",str.count('o'))
print("Find ",str.find("of"))
print()
 
#type of an object in string item
import string
print(string.digits)
print(string.ascii_letters)
"""To Fid the Details of Particular Function , we can print its documentation using the
docstring through _doc_ attribute
 
print(string.builtins_._doc_)
print()"""
 
#using help(): we can print the details of a particular item in the string module
str="hello"
print(help(str.isalpha))
print()
#type() shows the type of an object
#dir() shows the available methods
str="Hello"
print(dir(str))
print()
 
""" Regular Expression are a powerful tool for various kinds of string manipulatin .There are basically 
text string that is used for describing search pattern to extract information from text such as code,files,log
,spreadsheet or docs.
RE area a domain specific language(DSL) that is present as a library in most of the modern programming languages.
A regular expression is special sequence of characters that helps to match or find strings in another 
string.[import re]
-->match() function matches a pattern to a string (begining of the string) with optional flags.
 
Syntax: re.match(pattern,string,flags=0)
if the re.match() finds a match, it returns the match obect and none otherwise"""