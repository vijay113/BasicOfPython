
#List of my friends
friends = ["Vijay","Ram","Ajay","Sahil","Laxman"]
print(friends)

print(friends[0])
print(friends[2])
print(friends[1:])
print(friends[-2])  # from last index

print(friends[1:3])

print(friends.index("Ajay"))

print(friends.pop())
print(friends.pop())
print(friends.pop())
print(friends)

my_numbers = [1,2,3,4,5,6,7,8]

friends.extend(my_numbers)
print(friends)

friends.append("Gandhi")
print(friends)

print(len(friends))


friends.insert(2,"Titu")
print(friends)
print(len(friends))

friends.remove("Titu")
print(friends)

print(friends.count("Ram"))

my_numbers.sort()
print(my_numbers)
my_numbers.reverse()
print(my_numbers)

my_numberlist2 = my_numbers.copy()
my_numberlist2.extend(my_numbers)
print(my_numberlist2)
print(my_numberlist2.count(8))

my_numberlist2[0]="Start"
print(my_numberlist2)

friends.clear()
print(friends)

##############################
# Nested List

#######################
print("Nested List")
number_grid = [
   [1,2,3],
   [4,5,6],
   [7,8,9],
   [0]
]

print(number_grid)
print(number_grid[0][1])


for row in number_grid:
    for col in row:
        print(col)
    print("next row:")
print("End Loop")    


