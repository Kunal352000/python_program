str=input("Enter yur string: ")
words=str.split()
d={}
for i in words:
    d[i]=words.count(i)
print(d)
    
