num=int(input("Enter the number: "))
for i in range(num):
    for j in range(num+num-1):
        if i+j==4 or j-i==4:
            print("*",end="")
        else:
            print(" ",end="")
    print()

for i in range(num-1):
    for j in range(num+num-2):
        if j-i==1 or i+j==7:
            print("*",end="")
        else:
            print(" ",end="")
    print()
