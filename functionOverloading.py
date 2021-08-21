"""The concept of defining multiple functions with same name and differnet number
of parameters with in the same program is known as a function overloading"""
def f1():
    print("hey")
def f1(a):
    print("hello")
def f1(a,b):
    print("Good morning")
#f1()
#f1(4)
f1(4,5)
