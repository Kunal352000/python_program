num=int(input("Enter the numner: "))
s=0
temp=num
while num>=1:
    dig=num%10
    i=1
    f=1
    while dig>=i:
        f*=i
        i+=1
    s+=f
    num//=10

if temp==s:
    print("Given number is strong number.")
else:
    print("Given number is not strong number.")
    
