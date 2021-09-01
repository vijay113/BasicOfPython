
from collections import Counter, defaultdict, deque
from collections import namedtuple
from collections import OrderedDict

a = "aaabbcccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

print(my_counter.most_common())
print(my_counter.most_common(1)[0][0])


print(list(my_counter.elements()))

############################
##  NameTuple
##################

Point = namedtuple("Point","x,y")

my_point = Point(10,-20)
print(my_point)
print(my_point.x,my_point.y)

Student = namedtuple("Student","Name,Class,Age")
first_student = Student("Ajay","10th",21)
second_student = Student("Raam","12th",18)
print(first_student)
print(first_student.Name)
print(first_student.Age)
print(second_student.Name)

#################################
#
# Ordered Dictionary
###################################
 
my_dict = OrderedDict()
#my_dict = {"z":0}
my_dict["c"]=3
my_dict['a']=1
my_dict["b"]=2

print(my_dict)
print(my_dict["a"])
print(my_dict.keys())
print(my_dict.values())

######################
# Default Dictionary
#
#######################

default_dic = defaultdict(float)
#default_dic = {}
default_dic["a"]=10
default_dic["b"]=20
default_dic["c"]=30

print(default_dic)
print(default_dic["a"])
print(default_dic["z"])  # have default Value

################################
# Deque
#
##################

my_deque = deque()
my_deque.append(1)
my_deque.append(2)
my_deque.append(3)
my_deque.append(4)

print(my_deque)
my_deque.appendleft(5)
my_deque.appendleft(6)

print(my_deque)

my_deque.pop()
my_deque.popleft()
print(my_deque)

my_deque.extend([10,12,11])
my_deque.extendleft([-1,-2,-3])
print(my_deque)

my_deque.rotate(2)  # Right Shift
my_deque.rotate(-3) # Left Shift
print(my_deque)



