def f1():
    x=10
    def f2():
        nonlocal x
        print(x)
        x+=5
        print(x)
    f2()
    print(x)
f1()
