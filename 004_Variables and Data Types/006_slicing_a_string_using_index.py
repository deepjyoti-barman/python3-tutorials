# Platform             : GitHub
# Course Name          : python3-tutorials
# Company              : Go Digit General Insurance Limited
# Author               : Deepjyoti Barman
# Designation          : QA Analyst
# Date                 : September 28 (Monday), 2020




""" Program to demonstrate slicing of a string using index """

vod_website = 'YOUTUBE'

print('First character: ' + vod_website[0])
print('Last character: ' + vod_website[6] + '\n')
# print(vod_website[10])        # IndexError: string index out of range

print('First character in reverse order: ' + vod_website[-1])
print('Last character in reverse order: ' + vod_website[-7] + '\n')

print('Extracting the first 3 characters: ' + vod_website[0:3])
print('Extracting the middle 3 characters: ' + vod_website[1:4])
print('Extracting the last 4 characters: ' + vod_website[3:])
print('Extracting the first 4 characters: ' + vod_website[:4])
print('Extracting characters beyond the limit of the string: ' + vod_website[3:10])

# vod_website[0] = 'R'          # TypeError: 'str' object does not support item assignment (string in Python is immutable in nature)
