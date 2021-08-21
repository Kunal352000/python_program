num=int(input("Enter the number: "))
for i in range(num):
    for j in range(num+num-1):
        if i+j==4 or j-i==4:
            print("*",end="")
        elif i+j==5 or j-i==3 or i+j==6 or j-i==2 or\
             i+j==7 or j-i==1 or i-j==0:
            print("-",end="")
        else:
            print(" ",end="")
    print()
