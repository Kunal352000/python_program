#sum of digits
num=int(input("Enter a number=>"))
sum=0
while(num>0):
    r=num%10
    sum=sum+r
    num=num//10
print("Sum of digits=>",sum)
