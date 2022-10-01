#slice Operation 
num_list = [1,2,3,4,5,6,7,8,9]
print("First Element in the list is",num_list[0])
print("num_list[2:5]",num_list[2:5])
print("num_list[::5]",num_list[::5])
print("num_list[1:3]",num_list[1:3])
print()
 

 
#Updation of list
num_list3 = [1,2,3,4,5,6,7,8,9]
print("List is:",num_list3)
num_list3[5] = 100
print(num_list3)
num_list.append(200)
print(num_list3)
print()
 
#insert a list in another list
num_list4 = [1,8,9,7,56]
print("original list :",num_list4)
num_list4[2] = [4,5,6]
print("Updated list: ",num_list4)
print()
 
#nested list : a list within a list
list1 = [1,'a',"abc",[2,3,4,5],8,9]
i = 0
while i<(len(list1)):
    print("List1[",i,"]=",list1[i])
    i+=1
print()
 
#copy and clone of list
 
l1=[1,2,3,4,5,6,7,8,9]
l2 = l1
print("List1 =",l1)
print("List2 =",l2)
l3 = l1[2:6]
print("List3 =",l3)
print()
 
#All
 
l1 = [0,8,3,4]
l2 = [1,2,3,4,5,6,8,7,9]
print(l1)
print(all(l2))
print(any(l2))
 
#list keyword
l2 = list("Hello")
print(l2)
 
#Sorted
l3 = [3,4,1,2,7,8]
l4 = sorted(l3)
print(l4)
 
#insert(),remove() and sort() only modify the list, no return type
num_list = [100,200,300,400]
print(num_list.insert(2,250))
print(num_list)
print()
 
#sort method
list1 = ['l','a',"abc",'2','B',"Def"]
list1.sort()
print(list1)
print()
 
#delete items using empty list
list = ['p','r','o','g','r','a','m']
list[2:5] = []
print(list)
 
#Stack Operation in list
stack = [1,2,3,4,8]
print("original Stack",stack)
stack.append(7)
print("Stack after push operation is :",stack)
stack.pop()
print("Stack after pop operation is :",stack)
last_element_index = len(stack) - 1
print("value obtained after pop operation is :",stack[last_element_index])
print()
 
 
 
 
 
 
#make a list of cubes
cubes=[]
for i in range(11):
    cubes.append(i**3)
print("Cubes of Number from 1-10 ",cubes)
print()
 
"""Python supports computed lists called list comprehension
Syntax: List=expression for variable i sequence
Every list comprehension in python includes three elements:
1.Expression is the member itself ,a call to a methid or any other valid expression that returns a value.
The example below the expression i*3 is the square of the member value.
2.Member is the object or value in the list or iterable.In the above example,the member value is i.
3.Iterable is a list,set ,sequence,generator or  any other object tgat can return its element one at a time.
In the example beloq, the iterable is range(l1).
An iterable is an object that can be used repeatedly in subsequent loop statements"""
#empty list L=list()
cubes2=[i**3 for i in range(11)]
print(cubes2)
print()
 
#combine and print using list comprehension
print([(x,y) for x in [10,20,30] for y in [30,40,50] if x!=y])
print()
 





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
