"""python dont supporting function overloading concept because our python
interpreter to understand/recoginize last defined function only"""
def f1(*a):
    if len(a)==0:
        print("hello")
    if len(a)==1:
        print("kunal")
    if len(a)==2:
        print("good morning")
f1()
f1(1)
f1(1,2)
        
