import re

def validate_my_password(password):
    if re.search("[a-zA-Z0-9$#@]", password) and 6 <= len(password) <= 16: return True
    else: return False


# user enters the password until it satisfies the requirement
while True:
    password = input("\nEnter a password: ")
    if validate_my_password(password):
        print("Password Validation Success!")
        break
    else: print("Validation Failed!")