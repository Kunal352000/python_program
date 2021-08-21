x=eval(input("Enter the empty-nested list: "))
for i in range(2):
    for j in range(2):
        x[i].append(eval(input()))

print(x)
