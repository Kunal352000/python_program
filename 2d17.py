#adding two numbers in array
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
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ])
for i in range(3):
    for j in range(3):
        z[i][j]=x[i][j]+y[i][j]
    print()
for i in range(3):
    for j in range(3):
        print(z[i][j],end=" ")
    print()
