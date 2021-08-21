str=input("Enter your string: ").casefold()
words=str.split()
dic={}
for i in words:
    if i not in dic.keys():
        dic[i]=0
    dic[i]+=1
print(dic)
        
