x=[5,3,4,6,7,8,2]
y=filter(lambda x:x%2==0,x)
print(y)
for i in y:
    print(i)

print(tuple(filter(lambda x:x%2==0,[5,3,4,6,7,8,2])))
