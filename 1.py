x=[10,20,30,40,10,20,60,10]
print(x)
ele=int(input("Enter the element: "))
for i in range(len(x)):
    if x[i]==ele:
        print(i)
