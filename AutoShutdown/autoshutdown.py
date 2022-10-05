import os
shutdown = input("Do you want to shutdown the computer? (yes/no):  ")
if shutdown == 'yes':
    os.system("shutdown /s /t 1")
else:
    print('Shutdown is not required')


