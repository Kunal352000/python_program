num=int(input("Enter your number: "))
for i in range(num):
    for j in range(num):
        if i+j==2 or i-j==2 or\
           i+j==6 or j-i==2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
