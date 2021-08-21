class student:
    col_name='iglobal'
    col_add='ameerpat'
    def col_info(self):
        print(student.col_name)
        print(student.col_add)
s1=student()
s1.col_info()
print('*'*10)
print(student.col_name)
print(student.col_add)
print('*'*10)
print(s1.col_name)
print(s1.col_add)
