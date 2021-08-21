num=int(input("Enter the number: "))
s=0
temp=num
i=1
while num>=i:
    if num%i==0:
        s+=i
    i+=1

if s-temp==temp:
    print("Given number is perfect.")
else:
    print("Given number is not perfect.")
    
