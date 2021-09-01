import json
person = {"Name":"Ram","Age":20,"IsMale":True}

person_json= json.dumps(person, indent=4,sort_keys=True) #separators=(":","=")

print(person_json)

person1 = json.loads(person_json)
print(person1)

##########################
# Read Json from file
#######################

with open("person.json","r") as file:
    person = json.load(file)
    print(person)

#########################
# write in file
##############
# with open("person.json","w") as file:
#     json.dump(person,file,indent=4) 

###############################
# Encode Class into JSON
####################

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age


user = User("Raam",20)

# Encode using custom method:-

def encode_user(o):
    if isinstance(o,User):
        return {"Name":o.name, "Age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSON serializable.")


user_json = json.dumps(user,default=encode_user)
print(user_json)

#######################
# Encode using Custom Class
from json import JSONEncoder

class UserCustomEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o,User):
            return {"name":o.name,"age":o.age,o.__class__.__name__:True}
        else:
            super.default(self,o)


userjson1 = json.dumps(user, cls=UserCustomEncoder)
# OR
userJson2 = UserCustomEncoder().encode(user)
print(userjson1)
print(userJson2)

#########################
# Decode JSON into Python Object
########################

user_python = json.loads(userJson2)
print(type(user_python))  # this is not a object, this is Dictionary

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"],age=dct["age"])
    return dct

user_py = json.loads(userJson2,object_hook=decode_user)
print(type(user_py))
print(user_py.name, user_py.age)

########################################
######################################


###########################


