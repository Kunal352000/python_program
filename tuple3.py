t1=eval(input("Enter the element separted by comma "))
c=0
for i in t1:
    if c==t1.index(i):
        print(i,'  -  ',t1.count(i))
    c+=1
