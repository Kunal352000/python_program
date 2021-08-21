num=int(input("Enter your number: "))
x={}
for i in range(num):
    name=input("Enter your name: ")
    sal=int(input("Enter your salary: "))
    x[name]=sal
print(x)
