num=int(input("Enter your number: "))
no_of_dig=len(str(num))
s=0
temp=num
while num>=1:
    dig=num%10
    s=s+(dig**no_of_dig)
    num//=10

if temp==s:
    print("Given number is armstrong number.")
else:
    print("Given number is not a armstrong number.")
