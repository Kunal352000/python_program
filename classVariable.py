class student:
    col_name="iglobal"
    col_add="ameerpat"
    def std_info(self,sid,name):
        self.sid=sid
        self.sname=name
        print(self.sid)
        print(self.sname)
        print(student.col_name)
        print(student.col_add)
s1=student()
s1.std_info(101,"kunal")
s2=student()
s2.std_info(102,"shivam")
