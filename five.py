x=eval(input("Enter your nested list object: "))
for i in range(len(x)):
    for j in range(len(x)+i+1):
        x[i].append(eval(input()))
print(x)
