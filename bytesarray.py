x=[4,5,6,7]
print(x)
y=bytearray(x)
for i in y:
    print(i)
print(x)
y[1]=50
print("-"* 20)
for j in y:
    print(j)
