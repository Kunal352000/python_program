num=int(input("Enter the number: "))
for i in range(num):
    for j in range(i+1):
        print(chr(97+j),end=" ")
    print()