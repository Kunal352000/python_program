str=input("Enter your string: ")
words=str.split()
dic={}
for i in words:
    ch=i[0]
    if ch not in dic:
        dic[ch]=[]
    dic[ch].append(i)
print(dic)
