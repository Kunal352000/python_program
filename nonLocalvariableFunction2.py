def f1():
    x=10
    def f2():
        print(x)#10
        x+=5
        print(x)#error
    f2()
    print(x)#error
f1()
