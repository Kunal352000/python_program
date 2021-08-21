num=int(input("Enter the number: "))
i,j=0,1
c=1
while c<=num:
    print(i,end=" ")
    i,j=j,i+j
    c+=1
    
