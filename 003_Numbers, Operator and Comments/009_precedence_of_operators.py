# Platform             : GitHub
# Course Name          : python3-tutorials
# Company              : Go Digit General Insurance Limited
# Author               : Deepjyoti Barman
# Designation          : QA Analyst
# Date                 : April 06 (Monday), 2020




""" Program to demonstrate the order precedence of arithmetic operators in Python3 """

# Highest precedence at top, lowest at bottom
# Operators in the same level has evaluate Left to Right
# The order of precedence of arithmetic operators as follows:
# Parentheses                      : ()
# Exponentiation                   : **
# Positive, negative               : +x -x
# Multiplication, Division, Modulo : * / // %
# Addition, subtraction            : + -

result = 2 + (5 - 3) * 10 ** 2 // 8
print("2 + (5 - 3) * 10 ** 2 // 8 = ", result)