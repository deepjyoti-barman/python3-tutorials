# Platform             : GitHub
# Course Name          : python3-tutorials
# Company              : Go Digit General Insurance Limited
# Author               : Deepjyoti Barman
# Designation          : QA Analyst
# Date                 : April 05 (Sunday), 2020




""" Program to demonstrate the numeric types available """

# There are three different numeric types available in Python 3.8.2 [https://docs.python.org/3/library/stdtypes.html]
# int (plain integers): int represent positive or negative whole numbers
# integers takes up less space in memory
# e.g. 4, 57, -10
print("Value:", 9)
print("Type:", type(9))
print("------------------------------")

# float (decimal numbers): float represent real numbers, but are written with decimal points (or scientific notaion) to divide the whole number into fractional parts
# floating point numbers takes more space in memory
# e.g. 6.1, 1.333333, 5.0
print("Value:", 5.0)
print("Type:", type(5.0))
print("------------------------------")

# complex (complex numbers): complex numbers are represented by the formula a + bj, where a and b are floats, and j is the square root of -1 (the result of which is an imaginary number).
# e.g. 2+3j, 1+2j
print("Value:", 1+2j)
print("Type:", type(1+2j))
print("------------------------------")

# Note: Any operation performed between an int and a float always evaluate a float
print("5 + 6.0 =", 5 + 6.0)


"""
    NOTES:
    ------
    - type() method returns class type of the argument passed as parameter.
    - In other words, type() method to know which class a variable or a value belongs to.
    - type() method is mostly used for debugging purposes.
"""