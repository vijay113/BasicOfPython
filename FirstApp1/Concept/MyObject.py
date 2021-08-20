from MyClass import Student

student1 = Student("ajay","Business",3.0,False)

student2 = Student("Raaj","Computer",5.5,True)

print(student1.name)

print(student2.name)

print(student2.gpa)

print(student2.on_honor_roll())

print(student1.on_honor_roll())

#############################

from MyClass import Teacher,Staff


teacher = Teacher()
print(teacher.name)
print(teacher.get_salary()) 
# Methode inherited from Staff, Pick it's own value of Property 'Salary'

staff = Staff()
print(staff.get_salary())
# pick value of salary of Staff class


















