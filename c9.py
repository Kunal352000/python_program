#choice program
print('''
1.Add two numbers
2.Even Odd
3.Greater of two numbers
4.Area of circle
5.Exit''')
choice=int(input("Enter your choice=>"))
if(choice==1):
    x=int(input("Enter a number=>"))
    y=int(input("Enter a number=>"))
    sum=x+y
    print("Sum of this two number=>",sum)
elif(choice==2):
    x=int(input("Enter a number=>"))
    if(x%2==0):
        print(x,"is even number")
    else:
        print(x,"is odd number")
elif(choice==3):
    x=int(input("Enter a number=>"))
    y=int(input("Enter a number=>"))
    if(x>y):
        print("Greater number is x",x)
    else:
        print("Greater number is y",y)
elif(choice==4):
    r=float(input("Enter the radius=>"))
    area=3.14*r*r
    print("Area of circle=>",area)
elif(choice==5):
    print("Exit")
else:
    print("Enter choice b/w 1-5")
    
    
