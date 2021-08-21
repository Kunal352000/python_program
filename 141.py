x=[10,20,30,40,10,50,10,60,70,10,40]
print(x)
c=0
ele=int(input("Enter your element: "))
for i in x:
    if i==ele:
        c+=1
print(ele,"element is",c,"time in a list")

