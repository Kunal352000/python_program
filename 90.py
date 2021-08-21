num=int(input("Enter your number: "))
for i in range(num):
    for j in range(i):
        print("",end=" ")
    for j in range(num-i):
        print(num-i,end=" ")
    print()
