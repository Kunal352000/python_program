x=10#global variable
def f1():
    print(x)#10
    x+=5
    print(x)#error
f1()
print(x)#error
def f2():
    print(x)#error
f2()
