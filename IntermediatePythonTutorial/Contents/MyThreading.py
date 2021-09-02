
# Multiple Processing
#######################################
# from multiprocessing import Process
# import os
# import time

# def square_num():
#     for i in range(100):
#         i * i
#         time.sleep(0.1)


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

#########################################
# 
# Multi Threading
########################

# from threading import Thread
# import os
# import time

# def square_num():
#     for i in range(100):
#         i * i
#         time.sleep(0.1)


# threads = []
# num_threads = 10

# print(num_threads)

# # create thread

# for i in range(num_threads):
#     p = Thread(target= square_num)
#     threads.append(p)

# # start thread

# for p in threads:
#     p.start()

# # join Process
# for p in threads:
#     p.join()

# print("End Main")

#####################################
# share data between threads
##################################

from threading import Thread, Lock
import time

database_value = 0


def increase(lock):
    global database_value

    #lock.acquire()
    with lock:
        local_copy =  database_value
        #processing
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy
    #lock.release()

if __name__ == "__main__":

    lock = Lock()

    print("Start value", database_value)

    thread1 = Thread(target=increase,args=(lock,))
    thread2 = Thread(target=increase,args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("value is :", database_value)

    print("Main end")


###############################
#
# Queue
###########################

from queue import Queue
from threading import current_thread

# if __name__ == "__main__":

#     q = Queue()

#     q.put(1)
#     q.put(2)
#     q.put(3)

#     first = q.get()
#     print(first)
#     first = q.get()
#     print(first)
#     first = q.get()
#     print(first)

#     # q.empty()
#     # q.task_done()
#     # q.join()

#     print("End Main")


def worker(q,lock):
    while True:
        value = q.get()
        with lock:
            print(f" in {current_thread().name} got:{value}")
        q.task_done()

if __name__ == "__main__":
     
    lock = Lock()
    print("start main..")
    q1 = Queue()

    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker,args=(q1,lock))
        thread.daemon = True
        thread.start()

    for i in range(1,21):
        q1.put(i)
    
    q1.join()

    print("End Main")

#########################################
#########################################

