x=10
def f1():
    y=20
    global x
    x+=5
    def f2():
        z=30
        global x
        nonlocal y
        print(x)
        print(y)
        print(z)
        x+=5
        y+=5
        z+=5
        print(x)
        print(y)
        print(z)
    f2()
    print(y)
    print(x)
f1()
print(x)
