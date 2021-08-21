num=int(input("Enter the number: "))
for i in range(num):
    for j in range(num-1-i):
        print(" ",end="")
    for j in range(i+i+1):
        if i%2==0:
            print("*",end="")
        else:
            print("-",end="")
    print()
for i in range(num-1):
    for j in range(i+1):
        print(" ",end="")
    for j in range(num-1+num-2-i-i):
        if i%2==0:
            print("-",end="")
        else:
            print("*",end="")
    print()
