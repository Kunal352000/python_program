x=10#global
def f1():
    global x
    print(x)#10
    x+=15
    print(x)#25
f1()
print(x)#25
def f2():
    global x
    print(x)
    x+=10
    print(x)#35
f2()
print(x)
