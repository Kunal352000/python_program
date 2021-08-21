x=[]
num=int(input("Enter your number: "))
for i in range(1,num+1):
    if i%2==0:
        x.append(i)
    else:
        x.append("invalid")
print(x)
