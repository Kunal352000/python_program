str=input("Enter your string: ")
words=str.split()
d={}
for i in words:
    ch=i[0]
    if ch not in d:
        d[ch]=[]
    d[ch].append(i)
print(d)
