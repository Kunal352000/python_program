num=int(input("Enter the numner: "))
for i in range(num):
    for j in range(num-i):
        print("*",end=" ")
    print()
