x=[10,20,30,40,50,10,60,10,70,10]
ele=int(input("Enter your number: "))
c=0
for i in range(len(x)):
    if ele==x[i]:
        c+=1
print(c)
