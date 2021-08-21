class Employee:
    '''doc string(description)'''
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr

    def info(self):
        print(self.ename)
        print(self.eno)
        print(self.esal)
        print(self.eaddr)
e1=Employee(100,'Durga',10000,'hyd')
e1.info()
e2=Employee(200,'igloabl',20000,'ameerpat')
e2.info()
