print("Enter the number separted by comma ")
l1=[eval(i) for i in input().split(',')]
l1.sort()
print(l1[-2])
