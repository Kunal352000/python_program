num=int(input("Enter the number: "))
for i in range(num):
    for j in range(i):
        print(" ",end="")
    for j in range(num+num-i-i-1):
        print("*",end="")
    print()
