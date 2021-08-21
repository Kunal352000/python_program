str=input("Enter your string: ").casefold()
x={}
for i in str:
    if i in x:
        x[i]+=1
    else:
        x[i]=1
print(x)
    
    
