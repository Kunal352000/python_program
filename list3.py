x=[10,20,30,20,10,30,40,10,20,10,30,20]
y=[]
for i in range(len(x)):
    if x[i] not in y:
        y.append(x[i])
print("before removing=",x)
print("After removing=",y)
