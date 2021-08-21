class Employee:
    '''doc string(description)'''
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def info(self):
        print('*'*20)
        print("Employee number:",self.eno)
        print("Employee name:",self.ename)
        print("Employee salary:",self.esal)
        print("Employee address:",self.eaddr)
        print('*'*20)
e1=Employee(100,'durga',10000,'hyd')
e1.info()
e2=Employee(200,'pavan',20000,'chennai')
e2.info()
