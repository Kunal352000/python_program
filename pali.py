num=int(input("Enter your number:-"))
temp=num
rev=0

while num>=1:
    dig=num%10
    rev=(rev*10)+dig
    num=num//10

if rev==temp:
    print("given number is palindrome")
else:
    print("Given number is not palindrome")
