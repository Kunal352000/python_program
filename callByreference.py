"""in call by reference/pass by reference our original value is updated
in python we can implement call by reference by using indexing concept"""
x=[1,2,3]
def f1(y):
    print(y)
    y[0]=10
    y[1]=20
    y[2]=30
    print(y)
f1(x)
print(x)
