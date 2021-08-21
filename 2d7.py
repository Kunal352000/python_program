from numpy import*
x=array([
    [50,51,52],
    [60,61,62],
    [70,71,72],
    [80,81,82]
    ])
i=0
while(i<4):
    j=0
    while(j<3):
        print(x[i][j],end=" ")
        j+=1
    print()
    i+=1
