t=eval(input("Enter the numbers separted by comma: "))
i=0
for e in t:
    if i==t.index(e):
        print(e,' - ',t.count(e))
    i+=1
