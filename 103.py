x=input("Enter your string: ")
for i in range(len(x)):
    for j in range(i+1):
        print(x[j],end=" ")
    print()
