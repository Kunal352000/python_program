def f1():
    x=10
    def f2():
        global x
        x+=10
        print(x)
    f2()
    print(x)
f1()
print(x)
