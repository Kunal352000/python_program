x=input("Enter the string: ")
for i in range(len(x)):
    for j in range(i+1):
        print(x[::-1][j],end=" ")
    print()
