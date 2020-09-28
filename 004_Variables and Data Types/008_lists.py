# Platform             : GitHub
# Course Name          : python3-tutorials
# Company              : Go Digit General Insurance Limited
# Author               : Deepjyoti Barman
# Designation          : QA Analyst
# Date                 : September 29 (Tuesday), 2020




""" Demonstrate different ways of manipulating lists """

# List is a collection of values that can be of any type. Lists are very similar to arrays. A list can contain as many variables as you wish. Lists can also be iterated over in a very simple manner.

numbers = [20, 40, 10, 90]
names   = ['Ashish', 'Dj', 'Amisha', 'Asha']
values  = ['apples', 30, 'mangoes', 7.5]

# Printing a list
print('List of numbers:', numbers)

# Retrive first element of a list
print('First element:', numbers[0])

# Retrive last element of a list
print('Last element:', numbers[-1])

# Retrive the middle elements
print('Middle elements:',  numbers[1:3])

# Concatenating two lists
print('List of names:', names)
miscellaneous = [numbers, names]
print('Concatenation of two lists:', miscellaneous)

print('\n------------------------------------------------------------------------------------\n')

# OPERATION ON LISTS
# Lists are mutable [i.e. we can add, modify or remove elements from a list]
# Append: Adding an element at the end of a list
print('list.append(object)')
print("Before, values =", values)
values.append(50)
print('After, values  =', values)

print('\n------------------------------------------------------------------------------------\n')

# Insert: Adding an element at a specific position in the list
print('list.insert(index, object)')
print('Before, values =', values)
values.insert(2, 'grapes')
print('After, values  =', values)

print('\n------------------------------------------------------------------------------------\n')

# Remove: Removing an element from the list
print('list.remove(value)')
print('Before, values =', values)
values.remove(30)
print('After, values  =', values)

print('\n------------------------------------------------------------------------------------\n')

# Pop: Removing an element from the list based on the index number
print('list.pop(index)')
print('Before, values =', values)
values.pop(2)
print('After, values  =', values, '\n')

# Pop: Removing the last element of the list
print('list.pop()')
print('Before, values =', values)
values.pop()
print('After, values  =', values)

print('\n------------------------------------------------------------------------------------\n')

# Del: Removing multiple values from the list
print('del list[index]')
print('Before, values =', values)
del values[1:]
print('After, values  =', values)

print('\n------------------------------------------------------------------------------------\n')

# Extend: Addding multiple values at the end of the list
print('list.extend(iterable)')
print('Before, values =', values)
values.extend(['strawberry', '70', 'banana'])
print('After, values  =', values)

print('\n------------------------------------------------------------------------------------\n')

# Modification of a single list element
print('list[index] = value')
print('Before, names =', names)
names[0] = 'Nishant'
print('After, names  =', names, '\n')

# Modification of multiple elements
print('list[start-index:end-index] = iterable')
print('Before, names =', names)
names[1:3] = ['Krishna', 'Radha']
print('After, names  =', names, '\n')

# Modification of all the elements starting from an index
print('list[start-index:] = interable')
print('Before, names =', names)
names[2:] = ['Sandeep', 'Ruchi']
print('After, names  =', names, '\n')

# Modification of all the elements present before the index
print('list[:end-index] = interable')
print('Before, names =', names)
names[:3] = ['Roja', 'Mayank']
print('After, names  =', names, '\n')

print('\n------------------------------------------------------------------------------------\n')

# Finding the maximum element of a list
print('Maximum element:', max(numbers))

# Find the minimum element of a list
print('Minimum element:', min(numbers))

# Finding the sum of all the elements of a list
print('Sum of all the elements:', sum(numbers))

# Sorting all the elements of a list in ascending order
numbers.sort()
print("After sorting, numbers =", numbers)