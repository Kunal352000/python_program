x=eval(input("Enter the nested x-matrix: "))
y=eval(input("Enter the nested y-matrix: "))
z=eval(input("Enter the nested z-matrix: "))
print("Enter the element into x-matrix:")
for i in range(len(x)):
    for j in range(len(x)):
        x[i].append(eval(input()))
print("Enter the element into y-matrix: ")
for i in range(len(y)):
    for j in range(len(y)):
        y[i].append(eval(input()))
print("x matrix=",x)
print("y matrix=",y)
for i in range(len(z)):
    for j in range(len(z)):
        z[i].append(x[i][j]+y[i][j])
print("Result matrix is: ",z)
