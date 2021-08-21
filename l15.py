s=int(input("Enter the starting value: "))
e=int(input("Enter the ending value:"))
x=[]
for i in range(s,e):
    if i%7==0 and i%5!=0:
        x.append(i)
print(x)
