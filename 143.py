name=[]
marks=[]
for i in range(5):
    n=input("Enter the name: ")
    m=int(input("Enter the marks: "))
    name.append(n)
    marks.append(m)
h=max(marks)
m=min(marks)
print("Highest marks are=",h)
print("Lowest marks are=",m)
for i in range(5):
    if h==marks[i]:
        print("Student having highest marks is ",name[i])
    if m==marks[i]:
        print("Student having lowest marks is",name[i])
