x=[10,20,30,40,50,10,20,40,60,60]
y=[]
for i in x:
    if i not in y:
        y.append(i)
print(x)
print(y)
