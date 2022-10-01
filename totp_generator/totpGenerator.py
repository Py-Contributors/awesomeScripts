# Title :- TOTP Generator In Python

"""
    Purpose : Generate Time Based OTP (One Time Password)
    Author : Ajay
    Date : Fri 1, Oct, 2022
"""
import datetime
import pyotp

def totpGenerator():
    totp = pyotp.TOTP('base32secret3232')
    print(totp.now())
    time_remaining = totp.interval - datetime.datetime.now().timestamp() % totp.interval
    time_count = int(time_remaining)
    print("Time Remaining : " + str(int(time_remaining)) + " seconds")


if __name__ == '__main__':
    totpGenerator()
