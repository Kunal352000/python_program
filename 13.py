num=int(input("Enter your number: "))
x=list()
for i in range(1,num):
    if i%2==0 and i%3==0:
        x.append(i)
print(x)
