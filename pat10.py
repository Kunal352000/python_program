#pattern10
for i in range(1,6):
    for j in range(1,7-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*  ",end=" ")
    print()
