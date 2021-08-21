num=int(input("Enter your employee number: "))
d={}
for i in range(num):
    name=input("Enter employee name: ")
    sal=eval(input("Enter your salary: "))
    d[name]=sal
print("employee_name\tsalary")
for j in d:
    print(j,"\t\t",d[j])
