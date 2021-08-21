num=int(input("Enter the number of emplyees: "))
employee={}
for i in range(num):
    name=input("Enter the name of employee: ")
    salary=int(input("Enter the salary of employee: "))
    employee[name]=salary
print("\n\n employee_name\t salary")
for j in employee:
    print(j,"\t\t",employee[j])
