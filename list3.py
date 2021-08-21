x=[10,20,30,20,10,30,40,10,20,10,30,20]
y=[]
for i in x:
    if i not in y:
        y.append(i)
print(y)
