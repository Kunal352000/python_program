x=eval(input("Enter the nested list object: "))
for i in range(len(x)):
    for j in range(len(x)):
        x[i].append(eval(input()))
print(x)
