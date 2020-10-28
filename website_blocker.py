import time
from datetime import datetime as dt
hosts_path=r"C:\Windows\System32\drivers\etc"       #it contains host file it is for windows 

redirect = "127.0.0.1"
website_list=["www.facebook.com", " facebook.com","www.instagram.com"," instagram.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,5) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,12):
        print("Stay focused keep working")
        with open(hosts_temp, 'r+') as file:
        	content=file.read()
        	for website in website_list:
        		if website in content:
        			pass
        		else:
        			file.write(redirect+" "+ website+"\n")        
    else:
    	with open(hosts_temp,'r+') as file:
    		content = file.readlines()  # here content becomes a list
    		file.seek(0)
    		for line in content:
    			if not any(website in line for website in website_list):
    				file.write(line)
    		file.truncate()
    	print("Chill!! fun Hours")
    time.sleep(5)
