def arth_cal(x,y):
    return x+y,x-y,x*y,x/y
print(arth_cal(20,10))
print(type(arth_cal))

arth_cal1=lambda x,y:(x+y,x-y,x*y,x/y)
print(arth_cal1(10,5))
print(type(arth_cal1))
