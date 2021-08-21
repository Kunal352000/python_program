#in call by value/pass by value our original value is not modifed
x=10
def f1(y):
    print(y)
    y+=5
    print(y)
f1(x)
print(x)
print(y)
