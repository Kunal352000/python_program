class student:
    '''The class is developed by kj'''
    def __init__(self):
        print(id(self))
        
s=student()
print(id(s))
print("*"*20)
s1=student()
print(id(s1))
