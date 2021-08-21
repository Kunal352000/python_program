x=[10,20,30,40,10,20,30,40,10]
print(x)
ele=int(input("Enter your element: "))
y=[]
for i in range(len(x)):
    if ele == x[i]:
        pass
    else:
        y.append(x[i])
print(y)
