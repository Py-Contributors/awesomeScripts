t = ('foo','bar','baz','qux')
print(t)
print()
 
(s1,s2,s3,s4) = t   # (s1,s2,s3,s4) = ('foo','bar','baz','qux')
print(s1)
print(s2)
print(s3)
print(s4)
print()
 
(s1,s2,s3,s4) = ('foo','bar','baz','qux')
print(s1)
print(s2)
print(s3)
print(s4)
print()
 
(val1,val2,val3) = (2+4,5/3+4,9%6)
print(val1,val2,val3)
print()
 
def max_min(vals):
    x = max(vals)
    y = min(vals)
    return(x,y)
vals = (99,98,97,89,86,93,82)
(max_marks,min_marks) = max_min(vals)
print("Highest Marks = ",max_marks)
print("Lowest Marks = ",min_marks)
 
Toppers = (("Aman","B.Tech",91.9),("AB47CB","B.SC",96),("Psych","BCA",92.7))
for i in Toppers:
    print(i)
print()
 
Tup = (1,2,3,4,5,6,7,8)
print(Tup.index(4))
print()
 
tup = "dksjbhkjdfbkjlsdfhiljdhkldsfnhk;dfs",
print(type(tup))
print("d appears ",tup.count('d'),"times in",tup)
print()
 
Tup = 1,2,3,4,5
print(Tup)
print()
 
def display(*args):
    print(type(args))
    print(args)
Tup = (1,2,3,4,5,6)
display(Tup)
print()
 
Tup = (56,3)
 
quo,rem = divmod(*Tup)
print(quo,rem)
 
 
Tup = (1,2,3,4,5)
List1 = ['a','b','c','d','e']
print(list(zip(Tup,List1)))
print()
 
Tup = ((1,'a'),(2,'b'),(3,'c'))
for i,char in Tup:
    print(i,char)
print()
 
Tup = (5,1,0,2,36,87)
print(sorted(Tup))
print()
 
Tup = ("Heena",89,82.4)
print("%s got %d marks in CSA and her aggreate was %.2f" %(Tup[0],Tup[1],Tup[2]))


 
import functools #functions is a module that containi the function reduce()
num_list = [1,2,3,4,5,6,7]
print("Sum is values in list = ")
print(functools.reduce(lambda a,b:a+b,num_list))
print()
 

 
x = [[2,5,4],[1,3,9],[7,6,2]]
y = [[1,8,5],[7,3,6],[4,0,9]]
result = [[0,0,0],[0,0,0],[0,0,0]]
 
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]
for r in result:
    print(r)
print()
 
 
a = ['foo','bar','baz','qux','quux','corge']
print("Before appending :",a)
a += ['grault','garply']
print("After Appending : ",a)
print()
 
a = ['foo','bar','baz','qux','quux','corge']
print("Before prepending :",a)
a = [10,20] + a
print("After Prepending : ",a)
print()
 

 
a = ['foo','bar','baz','qux','quux']
print("Before appending with string: ",a)
a += 'corge'
print("After Prepending with string: ",a)
print()
 
a += ['corge']
print("After Prepending with string: ",a)
print()
 
def square(number):
    return number**2
number = [1,2,3,4,5]
squared = map(square,number)
print(list(squared))

 

def add_2(x):
    x+=2
    return x
num_list = [1,2,3,4,5,6,7]
print("Original list is :",num_list)
new_list = tuple(map(add_2,num_list))
print("Modified list is :",new_list)
print()
 
a1 = (1,2,3,4)
a1[1] = 100
print(a1)
 

 
num_list = [1,2,3,4,5]
it = iter(num_list)
for i in range(len(num_list)):
    print("Element at index",i,"is : ",next(i))
print()
 
 
#filter function
def check(x):
    if(x%2 == 0 or x%4 == 0):
        return 1
 
#call check()
evens = list(filter(check,range(2,22)))
print(evens)
print()
