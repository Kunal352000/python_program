def calculation(x,y):
    return x+y,x-y,x*y,x//y
print(calculation(10,5))

calculaton1=lambda a,b:(a+b,a-b,a*b,a//b)
print(calculaton1(20,5))
