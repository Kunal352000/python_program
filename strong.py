num=int(input("Enter any number:"))
temp=num
s=0
while num>=1:
    dig=num%10
    i=1
    f=1
    while i<=dig:
        f*=i
        i+=1
    s+=f
    num=num//10

if temp==s:
    print("Number is strong Number:")
else:
    print("Number is not strong number:")
    
