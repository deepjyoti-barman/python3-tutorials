# Platform             : GitHub
# Course Name          : python3-tutorials
# Company              : Go Digit General Insurance Limited
# Author               : Deepjyoti Barman
# Designation          : QA Analyst
# Date                 : April 05 (Sunday), 2020




""" Program to demonstrate string concatenation using format() method in Python3 """

# String concatenation using format() method
# Usage - 1
print("{}, {} and {} will remain best friends forever".format("Keerthi", "Deepjyoti", "Padmini"))

# Usage - 2
print("{2}, {1} and {0} will remain best friends forever".format("Keerthi", "Deepjyoti", "Padmini"))

# Usage - 3
print("{arg2}, {arg1} and {arg3} will remain best friends forever".format(arg1="Keerthi", arg2="Deepjyoti", arg3="Padmini"))

# format() method can be used to concatenate any type of operand
print("{} has won {} gold medals in the Olympics".format("India", 5))