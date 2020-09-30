import string 
import random
def urlshort(s):
    x = "cp.li"
    z = ".w"
    res = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    x = x+res+z
    return(x)
url = {}
n = int(input("Total Number of URLs you want to short : "))
while(n):
    s = input("Enter your Url : ")
    try:
        x = url[s]
    except:
        x = urlshort(s)
        url[s] = x
    print(x)
    n-=1
    