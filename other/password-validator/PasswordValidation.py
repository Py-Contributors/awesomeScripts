# Title :- Validating password
# import regular expression module
import re

# Taking Password from the user
inp = input("Input your password :")

con = True

while con:
    if(len(inp) < 7 or len(inp) > 15):
        break
    elif not re.search("[a-z]", inp):
        break
    elif not re.search("[0-9]", inp):
        break
    elif not re.search("[A-Z]", inp):
        break
    elif not re.search("[$#@]", inp):
        break
    else:
        print("Valid Password")
        con = False
        break

if con:
    print("Not a Valid Password")

''' Test cases :

    Input : 234@asdBNM
    Output : Valid Password

    Input : asdrtyjkl
    Output : Not a valid Password

'''
