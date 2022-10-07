#Author = P4ul x Cyberpj
#date : oct 3 2022
def enc():
    text=input(" Enter a plain text : ")
    nameoffile=input("save as : ")

    word_ord=[]

    secret_null=[]
    file=open(f'{nameoffile}',"w")
    for i in range(len(text)):
	    word_ord.append(ord(text[i]))


#print("word ord = ", word_ord)


    for j in word_ord:
	    secret_null.append("\u200b"*j)

    for i in range(len(secret_null)):
	    file.write(secret_null[i])
	    file.write("\n")
    file.close()
    print("file saved as : "+str(file.name))

def decoder():
    sec=''
    reader=input('enter a file name : ')
    encfile=open(reader,'rb')
    num=len(encfile.readlines())
    output=open('decoded.txt','w')
    anotherfile=open(reader,'r')
    for i in range(num):
        sec+=chr(len(anotherfile.readline())-1)
    output.write(sec)
    print(sec)
    output.close()
    anotherfile.close()
    encfile.close()

print('''\t\t\t\t
⠄⠄⠄\t\t⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠄⠄⠄⠄SECRETOR⠄⠄⠄⠄⠄⠄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀\t⠄⠄⠄ 
''')
inputer=int(input(" ENCODE = 1 \n DECODE = 2  \n >>>> "))
if(inputer==1):
	enc()
elif(inputer==2):
	decoder()
else:
	print("invalid input")

