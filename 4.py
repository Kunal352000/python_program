x=[10,20,30,10,10,20,30,40,50]
print(x)
y=[]
ele=int(input("Enter the number: "))
for i in range(len(x)):
    if x[i]==ele:
        pass
    else:
        y.append(x[i])
print(y)
