obj=eval(input("Enter your iterable object: "))
def my_len(x):
    c=0
    for i in x:
        c+=1
    print(c)
my_len(obj)
