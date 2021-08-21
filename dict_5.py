str=input("Enter your string: ").casefold()
d={}
for i in str:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
for j in d:
    print(j,":",d[j])
