num=int(input("Enter your number: "))
name=[]
marks=[]
for i in range(num):
    n=input("Enter the name: ")
    m=int(input("Enter the marks: "))
    name.append(n)
    marks.append(m)
h=max(marks)
l=min(marks)
print("Highest marks are ",h)
print("Lowest marks are ",l)
for i in range(num):
    if h==marks[i]:
        print("Student having maximum marks are-",name[i])
    if l==marks[i]:
        print("Student having minimum marks are-",name[i])
