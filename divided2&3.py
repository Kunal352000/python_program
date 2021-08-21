x=[1,23,7,8,11,45,33,22,10,6]
i=0
while i<len(x):
    if x[i]%2==0 and x[i]%3==0:
        print(x[i])
    i+=1
