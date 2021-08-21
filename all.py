x=[8,9.1,3j,"kunal"]
print(all(x))#true
y=[7,0,8,3]
print(all(y))#false
z=[True,0,9,False,2+3j]
print(all(z))#false
a=[0,False,True]
print(all(a))#false
b=[0,False]
print(all(b))#false
c="siva"
print(all(c))#true
d=34
print(all(d))#error int object is not iterable

