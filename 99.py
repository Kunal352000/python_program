num=int(input("Enter your number: "))
for i in range(num):
    for j in range(num-1-i):
        print("",end=" ")
    for j in range(i+1):
        print(chr(97+j),end=" ")
    print()
