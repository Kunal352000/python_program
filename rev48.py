num=int(input("Enter the number: "))
count=0
while num>=1:
    dig=num%10
    count+=1
    num//=10

print(count)
