obj=eval(input("Enter your iterable object: "))
def my_max(x):
    m=x[0]
    for i in x:
        if m<i:
            m=i
    print("Maximum element of your iterable object is",m)
my_max(obj)
