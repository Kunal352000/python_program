student=dict()
n=int(input("How many students are there: "))
for i in range(n):
    name=input("Enter the name of student: ")
    marks=[]
    for j in range(5):
        mark=float(input("Enter the marks of a student: "))
        marks.append(mark)
    student[name]=marks
print(student)
