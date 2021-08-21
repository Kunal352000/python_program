obj=eval(input("Enter your iterable object: "))
def my_min(x):
    m=x[0]
    for i in x:
        if m>i:
            m=i
    print("Minimum element your iterable object is",m)
my_min(obj)
