class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printName(self):
        print(self.firstname,self.lastname)

class Student(Person):
    pass

x=Student("Kunal","JOSHI")
x.printName()

y=Person("Priyansh","JOSHI")
y.printName()
