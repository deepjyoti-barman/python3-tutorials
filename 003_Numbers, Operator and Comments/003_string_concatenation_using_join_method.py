# Platform             : GitHub
# Course Name          : python3-tutorials
# Company              : Go Digit General Insurance Limited
# Author               : Deepjyoti Barman
# Designation          : QA Analyst
# Date                 : April 05 (Sunday), 2020




""" Program to demonstrate string concatenation using join() method in Python3 """

# String concatenation using join() method
# Syntax: "<delimiter>".join([str1, str2, str3, ..., strN])
print("-".join(["Hello", "World!"]))

# Note: Concatenation of a string with a numeric type is not possible
# print(" ".join([3, "Butterflies"]))         # Compile time error
# print(" ".join(["IPL", 2020]))              # Compile time error

# str() method cay be used to convert the numeric type into string type and then concatenate using join() method
print("".join(["I had ", str(4), " apples today"]))