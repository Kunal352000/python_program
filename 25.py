name=[]
mark=[]
num=int(input("Enter the your number: "))
for i in range(num):
    n=input("Enter your name: ")
    m=int(input("Enter your marks: "))
    name.append(n)
    mark.append(m)
h=max(mark)
l=min(mark)
print("highest mark:",h)
print("lowest mark:",l)
for i in range(num):
    if h==mark[i]:
        print("student having highest marks",name[i])
    if l==mark[i]:
        print("Student having lowest marks",name[i])
    
