# Platform             : GitHub
# Course Name          : python3-tutorials
# Company              : Go Digit General Insurance Limited
# Author               : Deepjyoti Barman
# Designation          : QA Analyst
# Date                 : April 06 (Monday), 2020




""" Program to demonstrate different uses of variables """

# Variables are like containers where we can store some data and use it by pulling it out later
# In other words, variable is a named symbol that holds a value
# Variables can hold all sort of things (data types) like numbers, booleans and strings
# Variables are useful: because of its reusability, its also useful while taking inputs dynamically from user
# Variables are always assigned with the variable name on the left and the value on the right of the equals sign
# Variables must be assigned before they can be used
no_of_cats        = 99
cats_gifted       = 2
remain_no_of_cats = no_of_cats - cats_gifted
print("The remaining number of cats are:", remain_no_of_cats)

# Variable re-assignment: Assigning variables to other variables at any time
present_no_of_friends = 100
new_friends           = 3
present_no_of_friends = present_no_of_friends + new_friends
print("My present number of friends:", present_no_of_friends)

# Multiple assignment
low, medium, high = 0, 5, 10
print(f"low = {low}, medium = {medium}, high = {high}")

# Chain assignment
tomato = potato = onion = 30
print(f"Price List: tomato = {tomato}, potato = {potato}, onion = {onion}")