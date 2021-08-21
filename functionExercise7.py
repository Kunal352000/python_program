obj=eval(input("Enter your iterable object: "))
def my_rev(x):
    y=[]
    for i in range(len(x)-1,-1,-1):
        y.append(x[i])
    print(y)
my_rev(obj)
        
