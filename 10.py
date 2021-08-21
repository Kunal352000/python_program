for i in range(4):
    for j in range(4-1-i):
        print(" ",end="")
    for j in range(i+i+1):
        print("*",end="")
    print()

for i in range(3):
    for j in range(i+1):
        print(" ",end="")
    for j in range(6-1-i-i):
        print('*',end="")
    print()
