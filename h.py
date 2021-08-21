l1=eval(input())
for i in range(3):
    for j in range(2):
        l1[i].append(eval(input()))
print(l1)
l1.sort()
print(l1)
print(max(l1))
