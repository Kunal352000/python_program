x=[0,5,10,15,20,25,30,35,40]
y=filter(lambda i:i%2==0,x)
print(y)
for i in y:
    print(i)

print(list(filter(lambda x:x%2==0,[0,5,10,15,20,25,30,35,40,45,50])))
