import os

#############
# write the file
################

# file = open("myfile.txt","w")
# file.writelines("this is my file")
# file.close()

file = open("myfile.txt")
print(file.read())
file.close()


################
# delete the file
#####################

os.remove("myfile.txt")

####################
# remove folder
#################
os.rmdir("demo")



