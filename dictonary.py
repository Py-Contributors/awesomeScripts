#Dictonaries
 
Dict = {}
print(Dict)
 
Dict = {x:2*x for x in range(1,10)}
print(Dict)
print()
 
Dict = {'Roll':'16/001','Name':'Sreya','Course':'B.Tech'}
print("Dict[Roll] = ",Dict['Roll'])
print("Dict[Name] = ",Dict['Name'])
print("Dict[Course] = ",Dict['Course'])
print()
 
Dict = {'Roll':'16/001','Name':'Sreya','Course':'B.Tech'}
if 'course' in Dict:
    print(Dict['courses'])
 
Dict = {'Roll':'16/001','Name':'Sreya','Course':'B.Tech'}
print(sorted(Dict.keys()))
 
Dict = {'Roll':'16/001','Name':'Sreya','Course':'B.Tech'}
print("Keys:",end=' ')
for key in Dict.keys():
    print(key,end=' ')
 
print("Values :",end = ' ')
for key in Dict.keys():
    print(key,end=' ')
 
print("\nDictonary : ",end = ' ')
for key,val  in Dict.items():
    print(key,val,"\t",end = " ")