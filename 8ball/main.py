import random

from pip._vendor.distlib.compat import raw_input


def obtainNumber():
    shakeResult = random.randint(1,8)
    return shakeResult


number = obtainNumber()
while True:
    shake = raw_input("Would you like to shake the 8 ball? ").lower()
    if shake == "yes":
        print("\n#############")
        print("#           #")
        print('#    ', number, '    #')
        print("#           #")
        print("#############")
    else:
        shake = raw_input("Would you like to shake the 8 ball? ").lower()
    break

if number == 1:
    print("It is certain")

elif number == 2:
    print("Outlook good")

elif number == 3:
    print("You may rely on it")

elif number == 4:
    print ("Ask again later")

elif number == 5:
    print ("Concentrate and ask again")

elif number == 6:
    print ("Reply hazy, try again")

elif number == 7:
    print("My reply is no")

elif number == 8:
    print("My sources say no")
