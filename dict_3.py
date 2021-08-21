str=input("Enter your string: ")
words=str.split()
d={}
for i in words:
    d[i]=len(i)
print(d)
    
