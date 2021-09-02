### Multiple Processing
######################################
from multiprocessing import Process, Value, Array, Lock
from multiprocessing import Queue
import os
import time

def square_num():
    for i in range(100):
        i * i
        time.sleep(0.1)


# processes = []
# num_processes = os.cpu_count()

# print(num_processes)

# # create process

# for i in range(num_processes):
#     p = Process(target= square_num)
#     processes.append(p)

# # start process

# for p in processes:
#     p.start()

# # join Process
# for p in processes:
#     p.join()

# print("End Main")


##########################
#
# Multiple Process using Array & value
##########################


# def add_100(numbers, lock):    
#         for i in range(100):
#             time.sleep(0.01)
#             # with lock:
#             #     number.value += 1
#             for i in range(len(numbers)):
#                 with lock:
#                     numbers[i] += 1


# if __name__ == "__main__":

#     lock = Lock()

#     shared_array = Array("d",[0.0,100.0,200.0])
#     #shared_number = Value("i",0)

#     print("Array at begining is : ", shared_array[:])
#     #print("Number at beginning is:", shared_number.value)

#     # p1 = Process(target=add_100,args=(shared_number,lock))
#     # p2 = Process(target=add_100,args=(shared_number,lock))

#     p1 = Process(target=add_100,args=(shared_array,lock))
#     p2 = Process(target=add_100,args=(shared_array,lock))


#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print("At the end , array is: ",shared_array[:])
#     #print("number at end is: ", shared_number.value)
#     print("End main")

##################################
#  Multiple Process using Queue
#####################################

# def square(numbers,queue):
#     for i in numbers:
#         queue.put(i*i)

# def make_negative(numbers,queue):
#     for i in numbers:
#         queue.put(-1 * i)


# if __name__=="__main__":
#     q = Queue()
#     numbers = range(1,6)
#     p1 = Process(target=square,args=(numbers,q))
#     p2 = Process(target=make_negative,args=(numbers,q))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     while not q.empty():
#         print(q.get())


#############################
#
#  Processing Process Pool
#
#################################

from multiprocessing import Pool

def cube(number):
    return number* number * number


if __name__=="__main__":

    number = range(10)

    my_pool = Pool()
    # map, apply, join, close

    result = my_pool.map(cube, number)

    # my_pool.apply(cube,number[0])   # only one number to execute by one pool

    my_pool.close()
    my_pool.join()

    print(result)

    #####################################
    ####################################







