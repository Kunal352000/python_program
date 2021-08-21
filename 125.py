num=int(input("Enter your number: "))
for i in range(num):
    for j in range(num+num-1):
        if i+j==4 or j-i==4:
            print("*",end="")
        else:
            print(" ",end="")
    print()
