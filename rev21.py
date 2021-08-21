x=int(input("Enter the value of x: "))
y=int(input("Enter the value of y: "))
z=int(input("Enter the value of z: "))
if z>x and z>y:
    print("z is greater.")
elif y>x and y>z:
    print("y is greater.")
elif x>y and x>z:
    print("x is greater.")
elif y==z and y>x:
    print("y and z is greater")
elif x==z and x>y:
    print("x and z is greater")
elif x==y and x>z:
    print("x and y is greater")
elif x==y and y==z:
    print("x,y and z is equal")
