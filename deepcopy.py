import copy
x=[1,2,3,[4,5,[6,7]]]
y=copy.deepcopy(x)
print(x)
print(y)
print(id(x))
print(id(y))
