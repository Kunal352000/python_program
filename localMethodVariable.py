class test:
    def m1(self):
        self.x=10#non-static variable
        y=20#local variable
        print(self.x)#10
        print(y)#20
    def m2(self):
        print(self.x)#10
        print(y)#nameError
t1=test()
t1.m1()
t1.m2()
