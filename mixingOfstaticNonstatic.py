class student:
    col_name="iglobal"#static variable
    col_add="ameerpat"#static varaible
    def std_info(self):
        self.sid=100#non-static
        self.sname="kunal"#non-static
        print(self.sid)
        print(self.sname)
        print(student.col_name)
        print(student.col_add)
s1=student()
s1.std_info()
