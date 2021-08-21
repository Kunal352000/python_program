from numpy import *
x=array([
        [50,51,52],
        [60,61,62],
        [70,71,72],
        [80,81,82]
        ])
i=3
while i>=0:
    j=2
    while j>=0:
        print(x[i][j],end=" ")
        j-=1
    print()
    i-=1
