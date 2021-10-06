# Python3 Cheatsheet

## Python Definition and Features

- Python is a interpreted, functional and object-oriented programming language.
- Interpreted = It involves no compilation steps, hence performance of a python application is really fast.
- Python supports both functional and object-oriented principals.
- Python is easy to learn because of its simple syntax.
- We can also develop applications quickly because of its inbuilt modules or libraries and Python can easily integrate any third party library.
- Python is dynamically typed. That is, we need not to specify what data type we are going to assign to a variable, Python is going to decide the type of a variable on runtime.
- Python has a huge community support.
- Instead of curly braces, Python uses indentation to recognize a block of code and as a standard or common-practice 4 spaces on the left is used by most programmers.

## First Python Program to Print 'Hello World'

```python
print('Hello World')
```

## Comments

- Single line comment:  

    ```python
    # This is a single line comment
    ```

- Multi-line comments / doc-strings (Document the author name, date, purpose of the code for other programmers):

    ```python
    '''
    This is one way
    of writing a
    multi-line comment
    '''

    """
    This is another way
    of writing a
    multi-line comment
    """
    ```

## Data Types

### Introduction

- A data types tells what type of data a variable can carry.
- In Python the data types are organized mainly into 7 types:
  - None: An object that does not contain any value
  - Numeric Types:
    - int
    - float
    - complex
  - Text Type:
    - str
  - Sequence Types:
    - list
    - tuple
    - range
  - Set Types:
    - set
    - frozenset
  - Mapping Type:
    - dict
  - Boolean Type:
    - bool
  - Binary Type:
    - bytes, bytearray, memoryview

### Numeric Types

```python
# int type
a = 13
b = -14
print(a, b)             # 13, -14
print(type(a))          # <class 'int'>

# float type
p = 10.5
q = -29.0
print(p, q)             # 10.5 -29.0
print(type(p))          # <class 'float'>

# complex type
d = 3 + 5j
print(d)                # (3 + 5j)
print(type(d))          # <class 'complex'>

# binary type
e = 0b1010              # 'b' can be in small or capital letter
print(e)                # 10

# hexadecimal type
f = 0xFF                # 'x' can be in small or capital letter
print(f)                # 255

# octal type
g = 0o17                # 'o' can be in small or capital letter
print(g)                # 15
```

### Boolean Type

```python
# bool type
a = True
b = (9 > 8)

print(b)                # True
print(type(b))          # <class 'bool'>
```

### Special Behaviors

```python
import keyword
print(keyword.kwlist)   # ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

print(True or False)    # True
print(True and False)   # False
print(True == 1)        # True
print(False == 0)       # True
print(True + True)      # 2
print(False + True)     # 1
print(None == 0)        # False
print(None == [])       # False
print(None == False)    # False

x = None
y = None
print(x == y)           # True

def getRes(x, y):
    z = x + y

result = getRes(5, 7)
print(result)           # None
```

### Type Conversion

```python
# float to int
a = 33.5
b = int(a)
print(b)                # 33
print(type(b))          # <class 'int'>

# string to float
c = float('22.7')
print(c)                # 22.7
print(type(c))          # <class 'str'>

# decimal to binary
print(bin(10))          # 0b1010

# decimal to hexadecimal
print(hex(10))          # 0xa

# decimal to octal
print(oct(10))          # 0o12
```

### Rules to Form an Identifier

- The names we give to the variables or functions are called identifiers.
- Python identifiers are case-sensitive.
- An identifier name can have numbers in middle or at the end, but it cannot start with a number.
- We can have any number of underscores (_) anywhere with-in an identifier name.
- We can't have special symbols like dollar ($) or pound (#) characters anywhere with-in the identifier name.
- We can't use keywords as an identifier name.

__Special Note__:

- `_var1` / `_func1()` : Private variable or private method
- `__var2` / `__func1()` : Really private variable or private method.
- `__init__` : Special function or a magic function.

### List, Set and Dictionary

- List: A list can store any number of values or objects dynamically and it maintains the order of them.
- Set: A set can store any number of values dynamically, but it does not allow duplicates.
- Dictionary: It is a map, can be used to store key and value pairs.

### Text Type

```python
str1 = 'You are awesome'
print(str1)

str2 = '''You are
the creator
of your destiny'''
print(str2)

# indexing: reaching out to a particular character or location in a string
# index always starts with 0 and goes till (length of the string - 1)
print(str1[2])          # u

# repetition: performing operation on the string several times
print(str1 * 2)         # You are awesomeYou are awesome

# retrieving the number of characters in a string
print(len(str2))        # 35
```

### String Manipulation

```python
str1 = 'You are awesome'

# SLICING
# syntax: str_var[beg_index:end_index:step] 
# get characters from 0 to 5
# it does not include the character at the ending index
print(str1[0:5])                        # You a

# get characters from 2nd position to the end
print(str1[2:])                         # u are awesome

# get characters from the beginning till the 8th position
print(str1[:8])                         # You are 

# get characters from the 3rd position from the end to the end
# -1 represents the last character of the string
print(str1[-3:-1])

# getting characters given a step
# by default the step value is 1
print(str1[0:9:2])                      # Yuaea

# get characters from the end to the beginning
print(str1[len(str1)::-1])              # emosewa era uoY
print(str1[::-1])                       # emosewa era uoY


# STRIPPING
# removing white-spaces from the beginning and the end of the string
str2 = '  Have a nice day     '
print(str2)                             #    Have a nice day     
print(str2.strip())                     # Have a nice day

# removing white-spaces from the beginning of the string
print(str2.lstrip())                    # Have a nice day     

# removing white-spaces from the end of the string
print(str2.rstrip())                    #    Have a nice day


# SEARCHING (CHARACTER / SUBSTRING)
# syntax: str_var.find(str_to_search:beg_index:end_index)
# find the location of a substring in a given string
# If find() is unable to get the substring then it returns -1
print(str1.find('awe'))                 # 10
print(str1.find('awe', 0, len(str1)))   # 10
print(str1.find('awe', 0, 8))           # -1


# COUNT OCCURRENCES (CHARACTER / SUBSTRING)
# syntax: str_var.count(str_to_search:beg_index:end_index)
# If count() is unable to get any occurrences of given substring then it returns 0
print(str1.count('a'))                  # 2
print(str1.count('a', 10, len(str1)))   # 0


# REPLACEMENT (CHARACTER / SUBSTRING)
# syntax: str_var.replace('old_str', 'new_str')
print(str1.replace('awesome', 'super')) # You are super


# SWITCHING CASES
print(str1.upper())                     # YOU ARE AWESOME
print(str1.lower())                     # you are awesome
print(str1.title())                     # You Are Awesome
```

### Sequence Type - List

```python
lst = [10, 20, 'Deepjyoti', -50, 80, 48.9]
print(lst)

# We can perform indexing, slicing and repetition on a list
# INDEXING
print(lst[3])                           # -50 

# SLICING
print(lst[3:5])                         # [-50, 80]

# REPETITION
print(lst * 2)                          # [10, 20, 'Deepjyoti', -50, 80, 48.9, 10, 20, 'Deepjyoti', -50, 80, 48.9]

# finding length of a list
print(len(lst))                         # 6

# adding an element to a list at the end
lst.append(77)
print(lst)                              # [10, 20, 'Deepjyoti', -50, 80, 48.9, 77]

# adding an element to a list at a given position
# index beyond the length of the list will add the new element at the end
# negative index will add the new element counting position from the end
lst.insert(0, 5)
print(lst)                              # [5, 10, 20, 'Deepjyoti', -50, 80, 48.9, 77]

# removing an element from the list by value
# if the element to be removed is not found the Python interpreter will throw ValueError
lst.remove('Deepjyoti')
print(lst)                              # [5, 10, 20, -50, 80, 48.9, 77]

# removing an element from the list by index
del(lst[3])                             # [5, 10, 20, 80, 48.9, 77]

# retrieving the maximum element in the list
print(max[lst])                         # 80

# retrieving the minimum element in the list
print(min[lst])                         # 5

# counting the occurrences of an element in a list
print(lst.count(20))                    # 1
print(lst.count(99))                    # 0

# retrieving the index of an element in a list
# if the given element is not found the Python interpreter will throw ValueError
print(lst.index(10))                    # 1

# sorting list in ascending order
lst.sort()
print(lst)                              # [5, 10, 20, 48.9, 77, 80]

# sorting list in descending order
lst.sort(reverse=True)
print(lst)                              # [80, 77, 48.9, 20, 10, 5]

# remove all the elements present in a list
lst.clear()
print(lst)                              # []
```

### Sequence Type - Tuple

- Tuple is just like a List data-structure, but it is immutable / read-only (i.e. once we create a tuple we can't modify it).
- A tuple maintains the insertion order.
- A tuple allows duplicate elements.
- We can add heterogeneous / different types of elements in a tuple.
- We can create a tuple by using parenthesis (). The parenthesis are optional, but it is recommended to use it as it is much more readable.
- If we have a single value in a tuple then we should always end it with a comma or else Python interpreter will treat it as a single element variable. (e.g. tup = 1, )

```python
tpl = (20)
print(tpl)                              # 20
print(type(tpl))                        # <class 'int'>

tpl = (20, )
print(tpl)                              # (20,)
print(type(tpl))                        # <class 'tuple'>

tpl = (20, 30, 20, 'xyz')
# tpl[2] = 123                          # TypeError: 'tuple' object does not support item assignment
print(tpl)                              # (20, 30, 20, 'xyz')
print(tpl * 2)                          # (20, 30, 20, 'xyz', 20, 30, 20, 'xyz')

# counting the occurrences of an element in a tuple
print(tpl.count(20))                    # 2

# retrieving the index of an element in a tuple
# if the given element is not found the Python interpreter will throw ValueError
print(tpl.index('xyz'))                 # 3

# get the last 3 elements of the tuple
print(tpl[-3:])                         # (30, 20, 'xyz')

# note: we can use all the methods of a list in a tuple which do not manipulate its elements

# conversion: tuple to list
lst = list(tpl)
print(lst)                              # [20, 30, 20, 'xyz']
print(type(lst))                        # <class 'list'>

# conversion: list to tuple
tpl = tuple(lst)
print(tpl)                              # 20, 30, 20, 'xyz')
print(type(tpl))                        # <class 'tuple'>
```

### List vs Tuple

- List uses square brackets to wrap a list of elements, whereas tuple uses parenthesis.
- For a list using square brackets are mandatory, whereas for a tuple its optional to use a pair of parenthesis.
- List is mutable, whereas tuple is immutable.
- List should be used in situations where we need to do manipulations on the elements, tuple should be used where consistency of the elements are mandatory.
- A list cannot be used as a key to the dictionary, because a dictionary key should be hashable and immutable, since tuple is immutable we can use tuple as a key to the dictionary.