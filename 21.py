a=[1,2,3,4]
b=[10,1,6]
print([a[i]+b[j] for i in range(len(a)) for j in range(len(b))])
