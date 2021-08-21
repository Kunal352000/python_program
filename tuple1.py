t1=eval(input("Enter the elements in tuple separted by comma "))
t2=eval(input("Enter the elements in tuple separted by comma "))
l1=list(t1)
l2=list(t2)
l1.sort()
l2.sort()
t1=tuple(l1)
t2=tuple(l2)
if t1==t2:
    print("tuple1.py")
else:
    print("tuple are not equal.")
