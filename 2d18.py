#adding two arrays
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
z=array([
    zeros(3),
    zeros(3),
    zeros(3)
    ])
for i in range(3):
    for j in range(3):
        z[i][j]=x[i][j]+y[i][j]
    
for i in range(3):
    for j in range(3):
        print(z[i][j],end=" ")
    print()
