num=int(input("Enter the number: "))
for i in range(num):
    for j in range(num):
        print(chr(65+j),end=" ")
    print()
