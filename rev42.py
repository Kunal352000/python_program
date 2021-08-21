num=int(input("Enter the number: "))
rev=0
temp=num
while num>=1:
    dig=num%10
    rev=(rev*10)+dig
    num//=10

if temp==rev:
    print("Given number is a palindrome.")
else:
    print("Given number is not a palindrome.")
