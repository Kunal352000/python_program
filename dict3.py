num=int(input("Enter your number: "))
print({i:i-1 for i in range(1,num+1) if i%2==0})
