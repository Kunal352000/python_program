#pattern13
k=8
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(1,k):
        print(" ",end=" ")

    k=k-2
    for j in range(i,0,-1):
        if(j!=5):
            print(j,end=" ")
    print()