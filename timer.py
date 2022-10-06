


# this will help to set you a particular time
#  within whichyou target to complete
#  the code and will give a countdown.


# import the time module
import time

# define the countdown func.
def countdown(t):
	
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1
	
	print('done!!!!!!')


# input time in seconds
t = input("Enter the time (in seconds): ")

# function call
countdown(int(t))
