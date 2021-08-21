from numpy import*
x=array([10,20,31,45,50])
y=array([11,20,30,40,55])

print(where(x>y,x,y))

print(where(x<y))
