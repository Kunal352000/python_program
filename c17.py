#prime number
num=int(input("Enter the number=>"))
for i in range(2,num):
    if(num%i==0):
        print("Number is not prime",num)
        break
else:
    print("Number is prime",num)
