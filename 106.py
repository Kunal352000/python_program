num=int(input("Enter your number: "))
for i in range(num):
    for j in range(num-i):
        print("*",end=" ")
    print()
for i in range(num-1):
    for j in range(i+2):
        print("*",end=" ")
    print()
