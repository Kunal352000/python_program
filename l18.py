names=[]
marks=[]
for i in range(5):
    n=input("Enter the names: ").capitalize()
    names.append(n)
    m=int(input("Enter the marks: "))
    marks.append(m)
h=max(marks)
l=min(marks)
print("Highest marks= ",h)
print("Lowest marks= ",l)
for i in range(5):
    if h==marks[i]:
        print(names[i],"having largest marks. ")
    if l==marks[i]:
        print(names[i],"having smallest marks. ")
