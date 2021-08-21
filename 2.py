num=int(input("Enter the number: "))
for i in range(num):
    for j in range(num-i):
        print("*",end="")
    print()
