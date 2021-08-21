str=input("Enter your string: ")
x={}
for i in str.split():
    x[i]=len(i)
print(x)
