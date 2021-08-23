
class Phone:
    def __init__(self) -> None:
        pass
    def set_color(self,color):
        self.color = color
    
    def set_cost(self, cost):
        self.cost = cost

    def show_color(self):
        return self.color

    def show_cost(self):
        return self.cost
    
    def make_call(self):
        print("Making Call...")

    def play_game(self):
        print("Game Playing...")


iphone = Phone()
sumsung = Phone()
iphone.set_color("Red")
iphone.set_cost(10000)

sumsung.set_color("Black")
sumsung.set_cost(5000)

print(iphone.show_color())
print(sumsung.show_color())
print(iphone.show_cost())
iphone.make_call()
sumsung.make_call()

###################################

class Employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print("salary of employee ",self.name, " is ", self.salary)


employee1 = Employee("Raam",10000)
employee2 = Employee("Ajay",5000)

employee1.show_details()
employee2.show_details()

########################
# Inheritance Class
#######################

# parent class
class Staff:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print("salary of staff named '",self.name, "' is ", self.salary)

# child class 1

class NonTeacher(Staff):
  
    def __init__(self, name, salary,task):
        super().__init__(name, salary)  
        self.task = task  

    def show_task(self):
        print("My task is ",self.task)    


# child class 2
class Teacher(Staff):
    def __init__(self,name,salary,subject):
        super().__init__(name,salary)
        #super().show_details()
        self.subject = subject
        #self.salary = salary
        #self.name = name

    def show_subject(self):
         print("subject of teacher is ", self.subject) 

    def show_details(self):
        print("this is override")
        return super().show_details() 


teacher1 = Teacher("Ravi",10000,"Hindi")

teacher1.show_details()
teacher1.show_subject()

bus_driver = NonTeacher("Ramu",2000,"Drive a bus")
#bus_driver = NonTeacher("Drive a Bus")
bus_driver.show_details()
bus_driver.show_task()

########################################
# #############
# Multiple Inheritance
# #############

class Parent1:
    def __init__(self,my_string1):
        self.string1 = my_string1
    def show_parent_1_string(self):
        print("1st Parent: "+self.string1)

class Parent2:
    def __init__(self,my_string2,address):
        self.string2 = my_string2
        self.address = address

    def show_parent_2_string(self):
        print("2nd Parent: "+self.string2)

    def show_parent_2_address(self):
        print("2nd Parent address: "+self.address)

class Child(Parent2,Parent1):
    def __init__(self, my_string1, child_string1,my_string2,address2):
        super().__init__(my_string2,address2) # second class parent string & address
        self.string1 = my_string1    # first class parent string
        self.child_string = child_string1       
        
 
    def show_child1_string(self):
        print("Child1 string:"+ self.child_string)    

child = Child("my 1st string","child's string","my 2nd string","2nd class address")
child.show_child1_string()
child.show_parent_1_string()
child.show_parent_2_string()
child.show_parent_2_address()


########################################

# Multi- level inheritance
##############################




class MyGrands:
    def __init__(self, string_grands):
        self.string_grands = string_grands
        self.salary = 10000

    def show_grands_details(self):
        print("we are your grands:"+ self.string_grands)   

    def show_salary(self):
        print("salary is:"+ str(self.salary)) 




class MyParent(MyGrands):
    def __init__(self,string_grands, string_parent):
        super().__init__(string_grands)
        self.string_parent = string_parent
        self.salary = 20000
        #self.show_parent_details()

    def show_parent_details(self):
        print("We are your parent:" + self.string_parent)

    # def show_salary(self):
    #     return super().show_salary()



class MyChild(MyParent):
    def __init__(self, string_grands, string_parent):
        super().__init__(string_grands, string_parent)
        self.child_string = "children"
        self.salary = 30000
 
    def show_child_detail(self):
        print("we are children:"+self.child_string)

    # def show_salary(self):
    #     return super().show_salary()

my_child = MyChild("love to grands","love to parents")
my_child.show_child_detail()
my_child.show_grands_details()
my_child.show_parent_details()
my_child.show_salary()


my_grands = MyGrands("i am grand father")
my_grands.show_salary()
my_grands.show_grands_details()

my_parent = MyParent("i am grand father","i am your father")
my_parent.show_salary()
my_parent.show_parent_details()



        
        
    
    








    

    


        





