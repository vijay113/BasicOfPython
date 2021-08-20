i = 1
while i<=10:
    print(i)
    i = i+1
print("Loop End.")
print(i)

####################
# Guessing Game #
####################
# secret_word = "Do"
# guess = ""
# try_count = 0
# try_max_count = 5
# guess_out = False
# print("Fill the blank below:-")
# print("Think before _____")
# while secret_word.lower() != guess.lower() and not(guess_out):
#     if(try_count < try_max_count):
#         guess = input("your answer is: ")
#         try_count += 1
#     else:
#         guess_out = True    

# if guess_out:
#     print("you lost the game")
# else:
#     print("You Win..!!")

###########################################
# For Loop
########################

my_friends = ["Ravi","Shyam","Raju","Ajay"]

for person in my_friends:
    print(person.upper())


my_months = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March"
}
print(my_months)
for month in my_months:
    print(my_months.get(month)) 
    print(month)  

for index in range(10):
    print(index)

for index in range(4,10):
    print(index)

for index in range(len(my_friends)):
    print(my_friends[index])

##################################





















