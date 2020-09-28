# Platform             : GitHub
# Course Name          : python3-tutorials
# Company              : Go Digit General Insurance Limited
# Author               : Deepjyoti Barman
# Designation          : QA Analyst
# Date                 : September 28 (Monday), 2020




""" Program to demonstrate the use of underscore (_) """

# Underscore _ is considered as "I don't Care" or "Throwaway" variable in Python

# The python interpreter stores the last expression value to the special variable called _.
# >>> 10 
# 10
# >>> _ 
# 10
# >>> _ * 3 
# 30


# The underscore _ is also used for ignoring the specific values. If you don’t need the specific values or the values are not used, just assign the values to underscore.

# Ignore a value when unpacking
x, _, y = (1, 2, 3)
print(f'Demonstration of ignorin the value: x = {x} and y = {y}')

# Ignore the index
for _ in range(3):     
    print("Demonstration of ignoring index")

# Ignore the argument
def demo(_):
    print('Demonstration of ignoring argument')

demo('Hello')