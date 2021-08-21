num=int(input("Enter your numbers: "))
x={}
for i in range(1,num+1):
    if i%2!=0:
        x[i]=i+1
print(x)
