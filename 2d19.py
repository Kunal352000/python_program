from numpy import*
x=array([
    [1,1],
    [2,2]
    ])
y=array([
    [1,1],
    [2,2]
    ])
z=array([
    zeros(2,int),
    zeros(2,int)
    ])
for i in range(2):
    for j in range(2):
        z[i][j]=x[i][j]+y[i][j]
for i in range(2):
    for z in range(2):
        print(z[i][j],end=" ")
    print()
