def f1(*x,y):
    print(x,type(x))
    print(y,type(y))
f1(2.3,4j,False,9)
#typeerror f1 missing 1 requires keyword-only argument:'y'
