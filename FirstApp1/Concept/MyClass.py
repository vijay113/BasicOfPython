

class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False    

#####################################

class Staff:
    def __init__(self):
        self.institute_name = "Arya College"
        self.salary = "10K"

    def get_salary(self):
        return self.salary

class Teacher(Staff):
    def __init__(self):
        self.name = "Mr. Ramesh Kumar"
        self.add = "London"
        self.phone = 190002
        self.is_qualified = True
        self.ask_for_tutorial= "No"
        self.salary = "40K"

    def get_staff_number(self):
        return self.phone

    


