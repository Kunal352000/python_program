for r in range(7):
    for c in range(5):
        if (c==0 or c==4) and r!=0 or\
           (r==0 or r==3) and (c==1 or c==2 or c==3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
        
