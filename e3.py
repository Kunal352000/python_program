num=int(input("Enter the number: "))
for i in range(num):
    for j in range(num):
        print(chr(97+i),end=" ")
    print()
