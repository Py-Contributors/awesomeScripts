import sys
import csv
import json

def csvtojson(file) -> str:
    f = open('{}.csv'.format(file),'r')
    l = list(csv.reader(f, delimiter=','))
    keys = l[0]
    dic = dict()
    js = []
    for i in range(1,len(l)-1):
        for j in range(len(keys)):
            dic[keys[j]] = l[i][j]
        js.append(dic.copy())

    with open('{}.json'.format(file),'a') as jfile:
        jfile.write(json.dumps(js, indent=4))

def jsontocsv(file) -> str:
    f = open('{}.json'.format(file))
    cv = json.load(f)
    df = open('{}.csv'.format(file), 'w', newline='')
    writeup = csv.writer(df)
    c = 0
    for data in cv:
        if(c==0):
            header = data.keys()
            writeup.writerow(header)
            c+=1
        writeup.writerow(data.values())
    df.close()

if __name__ == '__main__':
    if(sys.argv[1]=="-j"):
        jsontocsv(sys.argv[2].replace(".json",""))
    elif(sys.argv[1]=="-c"):
        csvtojson(sys.argv[2].replace(".json",""))
    elif(sys.argv[1]=="-h" or sys.argv[1]=="-help" or sys.argv[1]=="--h" or sys.argv[1]=="--help"):
        sys.stdout.write("usage: python [-j <path>] [-c <path>] [--help] \n\nYou can try following commands for various usage purpose \n\n   -j <path>    To convert Json File to CSV File\n   -c <path>    To convert CSV File to Json File\n   --h or --help    For help\n\nFor more information read README.md\nfile. You can also explore more commands.")
    else:
        sys.stdout.write("Invalid arguments \n\n* Type -h or -help for more \n")