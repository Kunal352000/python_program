num=int(input("enter your number: "))
for i in range(num):
    for j in range(num-i-1):
        print(' ',end="")
    for j in range(i+1):
        print(chr(97+j),end=" ")
    print()
