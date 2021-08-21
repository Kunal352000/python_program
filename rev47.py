num=int(input("Enter the number: "))
s=0
while num>=1:
    dig=num%10
    s=s+dig
    num//=10

print(s)
