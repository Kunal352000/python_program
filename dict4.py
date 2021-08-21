x=eval(input("Enter your list object: "))
y={}
for i in x:
    y[i]=x.count(i)
print(y)
