x=eval(input("Enter your nested list objects: "))
for i in range(len(x)):
    for j in range(len(x)):
        x[i].append(eval(input()))
print(x)
