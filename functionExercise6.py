obj=eval(input("Enter your iterable object: "))
def my_desc_ord(x):
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i]<x[j]:
                x[i],x[j]=x[j],x[i]
    print(x)
my_desc_ord(obj)

    
