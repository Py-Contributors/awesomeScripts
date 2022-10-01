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