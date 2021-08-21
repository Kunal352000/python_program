#Adding two array
from numpy import*
x=array([
    [1,1,1],
    [2,2,2],
    [3,3,3]
    ])
y=array([
    [1,1,1],
    [2,2,2],
    [3,3,3]
    ])
for i in range(3):
    for j in range(3):
        print(x[i][j]+y[i][j],end=" ")
    print()
