#operator
a=float(input("Enter the value of a=>"))
b=float(input("Enter the value of b=>"))
op=input("Enter operator +,-,*,/ =>")
if(op=='+'):
    result=a+b
    print("sum=",result)

elif(op=='-'):
    result=a-b
    print("sub=",result)

elif(op=='*'):
    result=a*b
    print("mul=",result)

elif(op=='/'):
    result=a/b
    print("div=",result)
else:
    print("Invalid Operator")

    
