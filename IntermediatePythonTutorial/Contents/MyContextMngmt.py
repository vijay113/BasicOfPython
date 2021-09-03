#####################################
# Context Manager
##############################

with open("sample_file.txt","w") as file:
    file.write("this is sample file")

##################################

file = open("sample_file_1.txt","w")
try:
    file.write("this is second sample file.")
except Exception as ex:
    print(ex)
finally:
    file.close()


##############################

from threading import Lock
lock = Lock()

lock.acquire()

a = 1
print(a)
lock.release()

# OR

with lock:
 a =1
 print(a)

############################
# Class for file management
##################################

class ManagedFile:
    def __init__(self,filename):
        print("init")
        self.filename = filename
        
    def __enter__(self):
        print("enter")
        self.file = open(self.filename,"w")
        return self.file

    def __exit__(self,exc_type,exc_value,exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print("error is occured.")
        print("exception:",exc_type,exc_value)
        print("exit")

with ManagedFile("sample_file_2.txt") as file:
    print("do something..")
    file.write("this is third sample file.") 
    # something()    
    print("process stop")

print("End program")

###################################
# using decorators
#####################################

from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename,"w")
    try:
        yield f
    finally:
        f.close()

with open_managed_file("sample_file_4.txt") as file:
    file.write("something to do..")

################################
#################################

