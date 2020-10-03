# use this command for turning keyboard up
import os
import time
UP = 'sudo /etc/acpi/asus-keyboard-backlight.sh'

# use this command to turn keyboard down
DOWN = 'sudo /etc/acpi/asus-keyboard-backlight.sh down'

password = 'jafrabad'
os.system('echo this script works')
os.system(f'echo {password} | -S {UP}')

delay = 0.1

while (True):
    time.sleep(delay)
    os.system(f'echo {password} | {UP}')
    time.sleep(delay)

    os.system(f'echo {password} | {UP}')
    time.sleep(delay)

    os.system(f'echo {password} | {UP}')
    time.sleep(delay)

    os.system(f'echo {password} | {DOWN}')
    time.sleep(delay)

    os.system(f'echo {password} | {DOWN}')
    time.sleep(delay)

    os.system(f'echo {password} | {DOWN}')
    time.sleep(delay)