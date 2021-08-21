num=int(input("Enter a number: "))
for i in range(num):
    for j in range(num-1-i):
        print(" ",end="")
    for j in range(num):
        print("*",end="")
    print()
