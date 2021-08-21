x=int(input("Enter x value: "))
y=int(input("Enter y value: "))
z=int(input("Enter z value: "))
if x>y and x>z:
    print("x is greater")
elif y>x and y>z:
    print("y is greater")
elif z>x and z>y:
    print("Z is greater than")
elif x<y and x<z and y==z:
    print("y,z is greater than")
elif x>y and z>y and x==z:
    print("x,z is graeter than")
elif x>z and y>z and x==y:
    print("x,y is greater than")
elif x==y and y==z and z==x:
    print("x,y,z is equal")
    
