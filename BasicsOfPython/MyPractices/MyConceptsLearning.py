class Base1():
    def __init__(self):
        self.str1 = "base1"
        print("base1")

        
class Base2():
    def __init__(self):
        self.str2 = "base2"
        print("base2")
        
class Derived(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
        #super().__init__()
        
    def print_str(self):
        print(self.str1,self.str2)
        
obj = Derived()
obj.print_str()


