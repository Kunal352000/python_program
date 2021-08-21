class student:
    '''The class developed by kj'''
    def __init__(self,rollno,name):
        self.name=name
        self.rollno=rollno
    def talk(self):
        print("Hello my name is ",self.name)
        print("Hello my rollnumber is ",self.rollno)
s=student(100,'kunal')
print(s.name)
print(s.rollno)
s.talk()

s1=student(200,'shivam')
s1.talk()

s2=student(300,'devashish')
s2.talk()
