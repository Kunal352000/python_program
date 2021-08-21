obj=eval(input("Enter your iterable object: "))
def my_sum(x):
    s=0
    for i in x:
        s+=i
    print("sum of your iterable object is =",i)
my_sum(obj)
