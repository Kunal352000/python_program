x=[10,20,30,40,50,10,20,10,80]
print(x)
ele=int(input("Enter the element: "))
y=[]
for i in range(len(x)):
    if x[i]==ele:
        pass
    else:
        y.append(x[i])
print(y)
