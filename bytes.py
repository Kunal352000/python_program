x=[4,5,6,7]
print(x)
y=bytes(x)
print(y)
for i in y:
    print(i)
print(x)
y[1]=50#TypeError:'bytes' object does not support item assignment
print(y)
