x=1
y=2
z=3
def f1():
    y=20
    z=30
    def f2():
        z=300
        print(x)
        print(y)
        print(z)
    f2()
    print(x)
    print(y)
    print(z)
f1()
print(x)
print(y)
print(z)
