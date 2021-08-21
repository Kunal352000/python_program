x=input("Enter your String: ")
for i in range(len(x)):
    for j in range(len(x)-1-i):
        print("",end=" ")
    for j in range(i+1):
        print(x[j],end=" ")
    print()
