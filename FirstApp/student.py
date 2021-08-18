class studentinfo:
    def __init__(self, name, rollnumber, marks):
        self.name= name
        self.rollnumber = rollnumber
        self.marks = marks
    
    def getname(self):
        print("Hello student")

class studentFamily(studentinfo):
    def __init__(self, name, rollnumber, marks):
        self.name= name
        self.rollnumber = rollnumber
        self.marks = marks
    
    def getfamilyname(self):
        print("Hello family ")        


class teacherinfo(studentFamily):
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
    # def getname(self):
    #     print("Hello teacher")
