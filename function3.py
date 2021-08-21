def f1(*x,y,**z):
    print(x,type(x))
    print(y,type(y))
    print(z,type(z))
f1(3.2,4j,True,name="kunal",age=21)
