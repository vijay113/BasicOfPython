import logging
#from logging import handlers
# logging.basicConfig(level=logging.DEBUG,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",datefmt="%m/%d/%Y %H:%M:%S")

# logging.debug("This is a debug message.")

# logging.info("This is an info message.")
# logging.warning("This is a warning message.")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

# #################################

# logger = logging.getLogger(__name__)
# logger.propagate = False
# logger.error("this is error in MyLogging.py")

# ##############################
# # Create Handler
# ###############################
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler("file.log")

# # level and format

# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")

# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# ##################################

# logger.warning("this is warning in MyLogging.py")
# logger.error("this is error in MyLogging.py")

#################################
#
# Logger config using dynamic FIle
#############################

# import logging.config

# logging.config.fileConfig("logging.conf")
# #logging.config.dictConfig("logging.conf")

# logger = logging.getLogger("simpleExample")

# logger.debug("debug message from MyLogging.py")


######################################
#
# STACK TRACEback
#
#########################################
# import traceback

# try:
#     a = [1,2,3]
#     #val = a[4]
# except IndexError as ex:
#     #logging.error(ex, exe_info= True)
#     logging.error("The Error is %s",traceback.format_exc())

#############################
###############################
# Rotating file handlers
#######################

# from logging.handlers import RotatingFileHandler
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# # Roll Over after 1kB and Keep Back up logs in 3 logging files:-
# handler= RotatingFileHandler("app.log",maxBytes=1000,backupCount=3)
# logger.addHandler(handler)

# for _ in range(10000):
#     logger.info("this is Info logging from MyLogging.py")


###############################
# 
# Time Rotating file Handler
###########################

from logging.handlers import TimedRotatingFileHandler
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#s = second ,m  = minutes , h = hour,d = day, midnight, w0 = monday, w1 = tuesday  etc...
handler = TimedRotatingFileHandler("time_test.log",when="s",interval=3,backupCount=4)
logger.addHandler(handler)

for _ in range(6):
    logger.info("This is time tested log from MyLogging.py")
    time.sleep(2)
###################################
###################################

# python JSON Logger can install n Use for large app.
###########################################







