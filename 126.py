num=int(input("Enter the number: "))
for i in range(num):
    for j in range(num+num-1):
        if i-j==0 or i+j==8:
            print("*",end="")
        else:
            print(" ",end="")
    print()
