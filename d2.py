str=input("Enter your string: ").casefold()
dic={}
for ch in str:
    if ch in dic:
        dic[ch]=dic[ch]+1
    else:
        dic[ch]=1
for i in dic:
    print(i,":",dic[i])
    
    
