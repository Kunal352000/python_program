#fibonaaciseries
n=int(input("Enter a number=>"))
a=1
b=0
for i in range(n):
    c=a+b
    print(c,end=" ")
    a=b
    b=c

print()
