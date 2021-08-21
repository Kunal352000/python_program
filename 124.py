num=int(input("Enter your number: "))
for i in range(num):
    for j in range(num+num-1):
        if i-j==0 or i+j==8:
            print("*",end="")
        elif j-i==1 or j-i==2 or i+j==7 or\
             i-j==3 or i+j==6:
            print("-",end="")
        else:
            print(" ",end="")
    print()    
