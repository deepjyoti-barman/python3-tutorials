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
  - Binary Types:
    - bytes
    - bytearray
    - memoryview

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
print(d.real)           # 3.0
print(d.imag)           # 5.0

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

# get the index of the substring if it is present in the string
# throws ValueError if the substring is not present in the string
# syntax: str.index(sub_string, <start_index>, <end_index>)
print(str1.index('are'))                # 4
print(str1.index('are', 4, 10))         # 4

# check if a substring is present at the end in the given string
print(str1.endswith('some'))            # True

# check if a substring is present at the beginning in the given string
print(str1.startswith('You'))           # True


# COUNT OCCURRENCES (CHARACTER / SUBSTRING)
# syntax: str_var.count(str_to_search:beg_index:end_index)
# If count() is unable to get any occurrences of given substring then it returns 0
print(str1.count('a'))                  # 2
print(str1.count('a', 10, len(str1)))   # 0


# REPLACEMENT (CHARACTER / SUBSTRING)
# syntax: str_var.replace('old_str', 'new_str')
print(str1.replace('awesome', 'super')) # You are super


# SWITCHING CASES
str3 = 'Winner Winner! Chicken dinner'
print(str3.upper())                     # WINNER WINNER! CHICKEN DINNER
print(str3.lower())                     # winner winner! chicken dinner
print(str3.casefold()                   # winner winner! chicken dinner
print(str3.title())                     # You Are Awesome
print(str3.capitalize())                # Winner winner! chicken dinner
print(str3.swapcase())                  # wINNER wINNER! cHICKEN DINNER


# DESIGN / ALIGNMENT
# adding width on both sides to center the text
print(str3.center(50))                  #           Winner Winner! Chicken dinner           


# STRING VALIDATIONS
print('abc123'.isalnum())               # True
print('abc 123'.isalnum())              # False
print('abcdef'.isalpha())               # True
print('ab12#$%-.lP'.isascii())          # True
print('203'.isdecimal())                # True
print('abcd'.isdecimal())               # False
print('904238'.isdigit())               # True
print('9042.38'.isdigit())              # False
print('abc1'.isidentifier())            # True
print'abc$'.isidentifier())             # False
print('1abc'.isidentifier())            # False
print('1ab,c'.islower())                # True
print('Cab2'.islower())                 # False
print('0123'.isnumeric())               # True
print('123.10'.isnumeric())             # False
print('Ab#91.33'.isprintable())         # True
print('     '.isspace())                # True
print('	a   '.isspace())                # False
print('You Are'.istitle())              # True
print('You are'.istitle())              # False
print('ABCDE'.isupper())                # True


# SPLITTERS
print('ABCDE'.partition('C'))           # ('AB', 'C', 'DE')
print('ABCDE'.partition('E'))           # ('ABCD', 'E', '')
print('ABCDE'.partition('A'))           # ('', 'A', 'BCDE')
print('ABCDE'.partition('F'))           # ('ABCDE', '', '')

print('ABCDE'.removeprefix('AB'))       # CDE
print('ABCDE'.removeprefix('AC'))       # ABCDE
print('ABCDE'.removesuffix('DE'))       # DE
print('ABCDE'.removesuffix('KE'))       # ABCDE

print('ABCDE'.split('C'))               # ['AB', 'DE']
print('ABCDE'.split('F'))               # ['ABCDE']
print('ABC\nDE'.splitlines())           # ['ABC', 'DE']
```

### Sequence Type - list

- A list type in Python is mutable in nature.

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

# reverse a list
lst.reverse()                           # [5, 10, 20, 48.9, 77, 80]

# add multiple elements in a list at the end
lst.extend([90, 99])                    # [5, 10, 20, 48.9, 77, 80, 90, 99]

# creating a deep copy of a list
lst2 = lst
print(lst)                              # [5, 10, 20, 48.9, 77, 80, 90, 99]
print(lst2)                             # [5, 10, 20, 48.9, 77, 80, 90, 99]

lst.remove(5)
print(lst)                              # [10, 20, 48.9, 77, 80, 90, 99]
print(lst2)                             # [10, 20, 48.9, 77, 80, 90, 99]

# creating a shallow copy of a list
lst3 = lst.copy()
print(lst)                              # [10, 20, 48.9, 77, 80, 90, 99]
print(lst3)                             # [10, 20, 48.9, 77, 80, 90, 99]

lst.remove(48.9)
print(lst)                              # [10, 20, 77, 80, 90, 99]
print(lst3)                             # [10, 20, 48.9, 77, 80, 90, 99]

# remove all the elements present in a list
lst.clear()
print(lst)                              # []
```

### Sequence Type - tuple

- tuple is just like a list data-structure, but it is immutable / read-only (i.e. once we create a tuple we can't modify it).
- A tuple maintains the insertion order.
- A tuple allows duplicate elements.
- We can add heterogeneous / different types of elements in a tuple.
- We can create a tuple by using parenthesis (). The parenthesis are optional, but it is recommended to use it as it makes the code much more readable.
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

### list vs tuple

- list uses square brackets to wrap a list of elements, whereas tuple uses parenthesis.
- For a list using square brackets are mandatory, whereas for a tuple its optional to use a pair of parenthesis.
- list is mutable, whereas tuple is immutable.
- list should be used in situations where we need to do manipulations on the elements, tuple should be used where consistency of the elements are mandatory.
- A list cannot be used as a key to the dictionary, because a dictionary key should be hashable and immutable, since tuple is immutable we can use tuple as a key to the dictionary.

### Set Types - set and frozenset

- A set type in Python is mutable in nature.
- The set sequence type does not allow duplicates.
- set does not maintain any order of its elements.
- We cannot perform indexing, slicing or repetition on a set.
- A frozenset does not allow add, update or remove operation in a set.
- A frozenset type in Python is immutable in nature.
- A set supports multiple other methods like union(), intersection(), difference(), isdisjoint(), issubset(), issuperset() etc.

```python
st = {10, 20, 30, 'xyz', 10, 20, 10}
print(st)                               # {'xyz', 10, 20, 30}
print(type(st))                         # <class 'set'>

# adding a new element into the set
st.add(5)
print(st)                               # {5, 10, 'xyz', 20, 30}

# adding multiple new elements to a set
st.update([88, 99])                     
print(st)                               # {99, 5, 10, 'xyz', 20, 88, 30}

# print(st[2])                          # TypeError: 'set' object does not support indexing
# print(st[0:5])                        # TypeError: 'set' object is not subscriptable
# print(st * 3)                         # TypeError: unsupported operand type(s) *: 'set' and 'int'

# removing element from a set
st.remove(99)                           
print(st)                               # {5, 10, 'xyz', 20, 88, 30}
# st.remove(45)                         # KeyError

# removing an element from a set if it is a member
st.discard(45)
print(st)                               # {5, 10, 'xyz', 20, 88, 30}
st.discard(88)
print(st)                               # {5, 10, 'xyz', 20, 30}

# removing an arbitrary element from the set
element = st.pop()
print(element)                          # 5
print(st)                               # {10, 'xyz', 20, 30}

# creating a shallow copy of a set
st2 = st.copy()
st.remove(30)
print(st)                               # {10, 'xyz', 20}
print(st2)                              # {'xyz', 10, 20, 30}

# INTERSECTION
st3 = st.intersection(st2)
print(st3)                              # {'xyz', 10, 20}

# DIFFERENCE
st3 = st2.difference(st)
print(st3)                              # {30}

# verify if another set contains this set
is_subset = st.issubset(st2)
print(is_subset)                        # True

# verify if this set contains another set
is_superset = st2.issuperset(st)
print(is_superset)                      # True

# removing all the elements from a set
st.clear()
print(st)                               # set()

fs = frozenset(st)
# fs.update([20])                       # AttributeError: 'frozenset' object has no attribute 'update'
# fs.remove(20)                         # AttributeError: 'frozenset' object has no attribute 'remove'       
```

### Sequence Type - range

- A range type in Python is immutable in nature.
- Syntax: `range(<start_value>, end_value, <step>)`

```python
# range with only one argument
r = range(5)
print(r)                                # range(0, 5)

for i in r:
    print(i, end=' ')                   # 0 1 2 3 4 

# range with two arguments
r = range(1, 6)

for i in r:
    print(i, end=' ')                   # 1 2 3 4 5 

# range with three arguments
r = range(1, 15, 3)

for i in r:
    print(i, end=' ')                   # 1 4 7 10 13 
```

### Binary Types - bytes and bytearray

- The maximum we can provide to a byte is 255.
- We cannot perform addition, modification or deletion operation in a bytes data type.
- We can perform addition, modification or deletion operation in a bytearray data type.
- No slicing or repetition is allowed on bytes or bytearray data types.
- Some important methods for bytes data type: count(), endswith(), find(), index(), join(), lower(), partition(), replace(), split(), startswith(), strip(), title(), upper()
- Some important methods for bytearray data type: append(), clear(), copy(), count(), endswith(), find(), index(), insert(), join(), lower(), partition(), pop(), remove(), replace(), reverse(), split(), strip(), title(), upper().

```python
lst = [20, 30, 40, 234]
print(type(lst))                        # <class 'list'>

b = bytes(lst)
print(b)                                # b'\x14\x1e(\xea'
print(type(b))                          # <class 'bytes'>

# b[3] = 22                             # TypeError: 'bytes' object does not support item assignment

b1 = bytearray(lst)
print(b1)                               # bytearray(b'\x14\x1e(\xea')
print(type(b1))                         # <class 'bytearray'> 

b1[3] = 22                              # No error
```

### Mapping Type - dict

- A dict type in Python is mutable in nature.
- The dict data type stores data in the form of key-value pair.
- The key and value both can be of any type.
- If same key is present two or more times then only the last value assigned to that key will be considered.

```python
dict1 = {
    1 : "john",
    2 : "bob",
    3 : "bill"
}
print(dict1)                            # {1: 'john', 2: 'bob', 3: 'bill'}
print(type(dict1))                      # <class 'dict'>

# accessing all the key-value pairs of the dictionary
kv_pairs = dict1.items()
print(kv_pairs)                         # dict_items([(1, 'john'), (2, 'bob'), (3, 'bill')])

# accessing all the keys of the dictionary
# keys() method only returns unique set of keys without any duplicates
k = dict1.keys()
print(k)                                # dict_keys([1, 2, 3])

for i in k:
    print(i, end=' ')                   # 1 2 3 

# accessing all the values of the dictionary
v = dict1.values()
print(v)                                # dict_values(['john', 'bob', 'bill'])

for i in v:
    print(i, end=' ')                   # john bob bill 

# accessing one value at time by key
print(dict1[2])                         # bob

# get the value for the key if the key is present in the dictionary else get None
value = dict1.get(4)
print(value)                            # None

value = dict1.get(3)
print(value)                            # bill

# create a new dictionary taking keys from the given iterable (list, tuple, set, range, map etc)
dict2 = dict1.fromkeys(range(5), 'dj')
print(dict2)                            # {0: 'dj', 1: 'dj', 2: 'dj', 3: 'dj', 4: 'dj'}

# same can be done using dict class
dict3 = dict.fromkeys(dict1)
print(dict3)                            # {1: None, 2: None, 3: None}

# insert key with a value (set to None when not given) if the key is not present and return the new value
# if the key is present return the value of the respective key
v1 = dict1.setdefault(4)
print(v1)                               # None
print(dict1)                            # {1: 'john', 2: 'bob', 3: 'bill', 4: None}

v2 = dict1.setdefault(5, 'mickey')
print(v2)                               # mickey
print(dict1)                            # {1: 'john', 2: 'bob', 3: 'bill', 4: None, 5: 'mickey'}

v3 = dict1.setdefault(3)
print(v3)                               # bill
print(dict1)                            # {1: 'john', 2: 'bob', 3: 'bill', 4: None, 5: 'mickey'}

dict1 = {
    1 : "john",
    2 : "bob",
    3 : "bill"
}

# update the dictionary with the elements from another dictionary object or from an iterable of key/value pairs
# if the given key is present update the value for the key in the dictionary
# if the given key is not present insert the key-value pair in the dictionary
dict1.update({1 : 'richard' })
print(dict1)                            # {1: 'richard', 2: 'bob', 3: 'bill'}

dict1.update({4 : 'peter'})
print(dict1)                            # {1: 'richard', 2: 'bob', 3: 'bill', 4: 'peter'}

# given a key remove the key-value pair from the dictionary and return the value
# throws KeyError if the key does not exist
val = dict1.pop(2)
print(val)                              # bob
print(dict1)                            # {1: 'richard', 3: 'bill', 4: 'peter'}

# remove and return a key-value pair as a tuple
# usually removes the last key-value pair
# throws KeyError when the dictionary is empty are we are calling this method to pop out a key-value pair
val = dict1.popitem()
print(val)                              # (4, 'peter')
print(type(val))                        # <class 'tuple'>
print(dict1)                            # {1: 'richard', 3: 'bill'}

dict1 = {
    1 : "john",
    2 : "bob",
    3 : "bill"
}

# removing a key-value pair from the dictionary
# throws KeyError if the key is not present in the dictionary
del(dict1[2])
print(dict1)                            # {1: 'john', 3: 'bill'}

del dict1[3]
print(dict1)                            # {1: 'john'}

# removing all the key-value pairs from the dictionary
dict1.clear()
print(dict1)                            # {}
```

### Immutability in Python

- When we define a variable in Python `a = 10` the PVM or Python Virtual Machine will store and allocate the memory for this value and the variable `a` will point to it. When we again declare a variable `b = 10`, PVM will first check if the value `10` is stored somewhere else in any memory location. If the memory location is found then PVM will not allocate new memory for the value `10` instead variable `b` will point to the same memory location pointed by variable `a`, saving us space. If we reassign a new value `b = 14` in this case PVM will store and allocate memory in a new location for this value and variable `b` will not point to it. This process is called immutability, where we cannot change the value in an existing memory location, instead a new memory location will be created whenever needed and the variable will point to that.
- Unlike Java, all primitive types and some object types in Python are immutable, whereas in Java only String object type is immutable.

```python
a = 10
b = 10

# retrieving the memory location of a
print(id(a))                            # 4353423952

# retrieving the memory location of b
print(id(b))                            # 4353423952

# comparing a and b by reference
print(a is b)                           # True

b = 20
print(id(b))                            # 4353424272
print(a is b)                           # False
```

### Special Types

- `None`: When we don't have any value to assign yet in a variable in our program, but still we want to assign some value to it - we can assign `None` to it.
- If a method in Python is not returning any value by default it will return None.
- An escape character is a character that invokes an alternative interpretation on the following characters in a character sequence.
- An escape character is a backslash \ followed by the character you want to insert.
- Some most used escape characters are \n, \t, \\" etc.
- In Java we have `final` keyword to declare a constant, in C or C++ we have a keyword `const` to declare a constant, but in Python we follow a convention where we will use all capital letters while naming a constant.
- `del` keyword can be used for cleanup or delete objects within our program.

```python
# None use-cases
a = None
print(a)                                # None

def m1():
    b = 10

print(m1())                             # None

# escape characters
print("He is known as \"God of All Time\"")         # He is known as "God of All Time"
print("Mike\t&\tTike are best friends")             # Mike	&	Tike are best friends

# constants
# this convention conveys the message to other developer that during their development they should to alter values for these variables
PI = 3.14
MAX_VALUE = 999
INTEREST_RATE = 7.3

# del keyword
c = 29
del c
# print(c)                              # NameError: name 'c' is not defined

# We can delete a string object, but we can't delete a character from it as str type is immutable in nature
s = 'abcd'
# del s[0]                              # TypeError: 'str' object doesn't support item deletion
```

## Operators and Operands

### Arithmetic Operators

- Arithmetic operators are:
  - Addition: +
  - Subtraction: -
  - Multiplication: *
  - Division: /
  - Remainder of a division / Modulo division: %
  - Exponent / Power: **
  - Integer division / Floor division: //

```python
a, b = 10, 4

print('a + b =', a + b)                 # a + b = 14
print('a - b =', a - b)                 # a - b = 6
print('a * b =', a * b)                 # a * b = 40
print('a / b =', a / b)                 # a / b = 2.5
print('a % b =', a % b)                 # a % b = 2
print('a ** b =', a ** b)               # a ** b = 10000
print('a // b =', a // b)               # a // b = 2
```

### Assignment Operators

- Assignment operators are:
  - Single equal / simple assignment: =
  - Compound assignment (with arithmetic operators): +=, -=, *=, /=, %=, **=, //=
  - Compound assignment (with bitwise operators): &=, |=, ^=, >>=, <<=

```python
# chain assignment
a = b = c = 10
print(a, b, c)                          # 10 10 10

# compound assignment
x, y = 10, 5
x += y
print(x)                                # 15
```

### Comparison Operators

- Comparison operators are:
  - Double equals / Equality / Equal to: ==
  - Not equal to: !=
  - Greater than: >
  - Less than: <
  - Greater than or equal to: >=
  - Less than or equal to: <=

```python
x, y = 77, 88

print(x == y)                           # False
print(x != y)                           # True
print(x > y)                            # False
print(x < y)                            # True
print(x >= y)                           # False
print(x <= y)                           # True
```

### Logical Operators

- Logical operators always work with boolean values (operands are of bool type).
- Logical operators are:
  - AND: and
  - OR: or
  - NOT: not

```python
x, y = 20, 30

print(x == 20 and y == 30)              # True
print(x == 25 and y == 30)              # False

print(x == 25 or y == 30)               # True
print(x == 25 or y == 31)               # False

print(not(x == 25 or y == 31))          # True
```

### Bitwise Operators

- Bitwise operators are:
  - Bitwise AND: &
  - Bitwise OR: |
  - Bitwise NOT: ~
  - Bitwise XOR: ^
  - Bitwise right shift: >>
  - Bitwise left shift: <<

```python
# x = 10 = (0000 1010) in binary
x = 10

# y = 4  = (0000 0100) in binary
y = 4

# (0000 0000)
print(x & y)                            # 0

# (0000 1110)
print(x | y)                            # 14

# (0000 1110)
print(x ^ y)                            # 14

# (1111 0101) = 2's complement => -11
print(~x)                               # -11

# (0000 0010)
print(x >> 2)                           # 2

# (0010 1000)
print(x << 2)                           # 40
```

### Membership Operators

- Membership operators are used to check an item or an element that is part of a string, a list, a tuple or any sequence.
- Membership operators are:
  - in - Returns true, if item is present in the list or sequence.
  - not in - Returns true, if item is not present in the list or sequence.

```python
print(10 in [20, 10, 30, 60])           # True
print('s' in 'switzerland')             # True
print(4 not in range(1, 20))            # False
```

### Identity Operators

- Identity operators are used to check whether reference of both operands are same or not.
- Identity operators are:
  - is - Returns true, if reference of both the operands are same.
  - is not - Returns true, if reference of both the operands are different.

```python
a = 10
b = 10
c = 20

print(a is b)                           # True
print(b is c)                           # False
print(a is not c)                       # True
```


### Precedence of Operators

- Following is the operator precedence table in lower to higher order:

| Operator                        | Description                                                |
| :------------------------------ | :--------------------------------------------------------- |
| NOT, OR, AND                    | Logical operators                                          |
| in, not in                      | Membership operators                                       |
| is, not is                      | Identity operators                                         |
| =, %=, /=, //=, +=, -=, *=, **= | Assignment operators                                       |
| <>, ==, !=                      | Equality operators                                         |
| >, <, >=, <=                    | Comparison operators                                       |
| ^, \|                           | Bitwise XOR, Bitwise OR operator                           |
| &                               | Bitwise AND operator                                       |
| <<, >>                          | Bitwise left shift, Bitwise right shift operator           |
| +, -                            | Addition, Subtraction operator                             |
| *, /, %, //                     | Multiplication, Division, Modulus, Floor division operator |
| **                              | Exponential operator                                       |

## Input and Output Functions

```python
# different use of print() function
print()                                 # adds an empty newline
print('Hello')                          # Hello
print('Hello ' * 3)                     # Hello Hello Hello
print('India \nis the best')            # India
                                        # is the best

item, price = 'apple', 70
print(item, price)                      # apple 70
print(item, price, sep=' | ')           # apple | 70
print('Hello', end=' ')
print('World')                          # Hello World

# STRING FORMATTING
# using addition operator
print('An ' + item + ' costs ' + str(price) + ' rupees per kilo')           # An apple costs 70 rupees per kilo

# using comma operator
print('An', item, 'costs', price, 'rupees per kilo')                        # An apple costs 70 rupees per kilo

# using modulo operator
print('An %s costs %i rupees per kilo' % (item, price))                     # An apple costs 70 rupees per kilo

# using format method
print('An {} costs {} rupees per kilo'.format(item, price))                 # An apple costs 70 rupees per kilo
print('An {1} costs {0} rupees per kilo'.format(price, item))               # An apple costs 70 rupees per kilo
print('An {arg0} costs {arg1} rupees per kilo'.format(arg0=item, arg1=price))   # An apple costs 70 rupees per kilo

# using join method
print("".join(['An ', item, ' costs ', str(price), ' rupees per kilo']))    # An apple costs 70 rupees per kilo

# using f-string (The best and most recommended way)
print(f'An {item} costs {price} rupees per kilo')
```

```python
# reading input from user without a message
name = input()                                  # Deepjyoti
print(name)                                     # Deepjyoti

# reading input from user with a message
occ = input('What is your occupation? ')        # What is your occupation? Student
print(occ)                                      # Student

# reading integer input from user
age = int(input('How old are you? '))           # How old are you? 28
print(age)                                      # 28
print(type(age))                                # <class 'int'>

# reading multiple inputs from the user using input()
num_list1 = [x for x in input('Enter any three number separated by space: ').split()]    # Enter any three number separated by space: 1 2 3
print(num_list1)                                # ['1', '2', '3']


num_list2 = [float(x) for x in input('Enter any three number separated by comma: ').split()]    # Enter any three number separated by space: 1.4,2.7,3.9
print(num_list1)                                # [1.4, 2.7, 3.9]
```

```python
# program: find the area of a circle reading the radius from the end-user
import math

radius = float(input('Enter the radius of the circle: '))          # Enter the radius of the circle: 5
# area = math.pi * radius ** 2
area = math.pi * math.pow(radius, 2)
print('Area of the circle: %.2f' % area)        # Area of the circle: 78.54
```

## Flow Control Statements

- Flow control determines the order in which the statements are executed at runtime.
- They are categorized into:
  - Conditional statements
  - Iterative / looping statements
  - Transfer statements
- Conditional Statements: Allows us to execute our code conditionally (i.e based on a given condition). These are:
  - if
  - if..else
  - if..elif..else (if-else ladder)
- Looping Statements: Allows us to execute same set of statements or logics multiple times. These are:
  - while
  - for
- Transfer Statements: Allows us to transfer the control of our program from one place to another. These are:
  - break
  - continue
  - pass
  - return

### if / if..else / if..elif..else

```python
num = int(input('Enter any number: '))          # Enter any number: 4

# if
# checking if the number is even
if num % 2 == 0:
    print(f'{num} is even')                     # 4 is even

# if..else
# checking if the number is even or odd
if (num % 2 == 0):
    print(f'{num} is even')                     # 4 is even
else:
    print(f'{num} is odd')

# if..elif..else
# checking if the number is even, odd or a zero
if num == 0:
    print(f'{num} is neither odd nor even')
elif num % 2 == 0:
    print(f'{num} is even')                     # 4 is even
else:
    print(f'{num} is odd')
```

### while loop

```python
num = 1

# while
# printing values from 1 to 20
while (num <= 20):
    print(num, end=' ')                         # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
    num += 1
```

```python
# program: print all odd numbers in a given range
start = int(input('Enter the starting number of the range: '))      # Enter the starting number of the range: 2
end   = int(input('Enter the ending number of the range: '))        # Enter the ending number of the range: 9

if start % 2 == 0:
    start += 1

while start <= end:
    print(start, end=' ')                       # 3 5 7 9 
    start += 2
```

### for loop

- A for loop in Python is a sequence based loop (i.e. it works only with sequences).
- A for loop is typically used to iterate over the elements of a sequence like string, list, tuple, set, range etc.

```python
# for
# printing values from 50 to 70
for i in range(50, 71):
    print(i, end=' ')                           # 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 
```

### break

```python
# break
# break out of the loop if number 5 is present in the loop, else print all the elements
lst = [1, 4, 9, 7, 5, 2, 8]

for i in lst:
    if i == 5:
        break
    print(i, end=' ')                           # 1 4 9 7
```

### continue

```python
# continue
# print 1 to 20 while skipping multiples of 3
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i, end=' ')                           # 1 2 4 5 7 8 10 11 13 14 16 17 19 20 
```

### assert

- assert will abnormally terminate the flow of a program raising an AssertionError if the condition given next to this statement found to evaluate `False`.

```python
# validate if the number given by the end-user is greater than 10
num = int(input('Enter any number greater than 10: '))      # Enter any number greater than 10: 2

assert num > 10, 'Wrong number entered'         # AssertionError: Wrong number entered
print('PASS - you have entered', num)
```

### pass

- In Python, pass is a null statement. The interpreter does not ignore a pass statement, but nothing happens and the statement results into no operation.
- The pass statement is useful when you don’t write the implementation of a function but you want to implement it in the future.
- pass primarily used to avoid compilation errors, when some code block is left empty. It has become a need for the programmers because unlike other languages Python do not use curly braces {} to identify an empty block without any statements.

```python
# pass (example - 1)
def addition(num1, num2):
    pass

addition(2, 2)

# pass (example - 2)
# prints the number if it is not 2
number = 3
if number == 2:
    pass
else:
    print ('Number: ', number)                  # Number: 3
```

### return

- The return statement is used to return values from functions / methods.

```python
def getName():
    name = input('What is your name? ')         # What is your name? Deepjyoti
    return name

nm = getName()
print('Nice to meet you %s' % nm)               # Nice to meet you Deepjyoti
```

### eval

- eval is a built-in function used in Python.
- eval function parses the expression argument and evaluates it as a Python expression. In simple words, the eval function evaluates the "String" like a python expression and returns the result as an integer.
- Syntax: `eval(expression, [globals[, locals]])`
- Arguments and parameters: The arguments or parameters of eval function are strings, also optionally global and locals can be used as an argument inside eval function, but the globals must be represented as a dictionary and the locals as a mapped object.
- Return value: The return value would be the result of the evaluated expression. Often the return type would be an integer.

```python
num = eval(input('Enter any number of your choice: '))      # Enter any number of your choice: 10 + 10
print(num)                                                  # 20
print(type(eval))                                           # <class 'int'>
```

### Practice Programs

```python
# program: remove duplicate elements from a list
l1 = eval(input('Enter a list of elements: '))              # Enter a list of elements: [10, 20, 30, 40, 30, 20]
l2 = []

for each_value in l1:
    if each_value not in l2:
        l2.append(each_value)

print('List of unique elements:', l2)                       # List of unique elements: [10, 20, 30, 40]
```

```python
# program: count the number of vowels in a given word
word = input('Enter a word: ')                              # Enter a word: eagle
vowels = {'a', 'e', 'i', 'o', 'u'}
results_dict = {}

for char in word:
    if char in vowels:
        # Syntax: dict.get(key, default=None)
        results_dict[char] = results_dict.get(char, 0) + 1

for key, values in sorted(results_dict.items()):
    print(f'{key} is present {values} time(s)')             # a is present 1 time(s)
                                                            # e is present 2 time(s)
```

```python
# program: reverse a string
# approach_1
str1 = input('Enter a string: ')                            # december
print('Revered string:', str1[::-1])                        # Revered string: rebmeced

# approach_2
print('Revered string:', ''.join(reversed(str1)))           # Revered string: rebmeced

# approach_3
lst = list(str1)
lst.reverse()
print('Reversed string:', ''.join(lst))                     # Reversed string: rebmeced
```

```python
# program: print right angled triangle pattern
rows = int(input('Enter the number of rows for the pattern to expand: '))

# approach - 1
for i in range(rows):
    for j in range(i + 1):
        print('*', end=' ')
    print()

# approach - 2 (the python way)
for i in range(rows):
    print('* ' * (i + 1))
```

```python
# program: print pyramid pattern
rows = int(input('Enter the number of rows for the pattern to expand: '))

for i in range(rows):
    print(' ' * rows - i)
    print('* ' * i + 1)
```

```python
# program: find substring in given string
s = 'Take up one idea and make that idea your life. Think and dream of that idea and leave every other idea alone.'
subs = 'idea'
pos = -1
length = len(s)

while True:
    pos = s.find(subs, pos + 1, length)

    if pos == -1:
        break;
    
    print('Found the substring at position: ', pos)
    found = True

if found == False:
    print('Substring is not found')
```

## Command Line Arguments

- The command line arguments are those arguments that are passed when our Python program is run.  
  `> python3 my_program.py 123 abc xyz`
- Main uses of command line argument could be:
  - Passing in a 'File location' dynamically at the runtime (instead of hard-coding it inside our program).
  - Passing in a 'Database name' or 'Connection URL'
  - Passing in a 'Remote IP address'
- The values passed at runtime from command line are saved in a list called 'argv', which is present inside 'sys' module.

```python
# program: calculate the product of all the command line arguments passed
import sys

prod = 1
for i in range(1, len(sys.argv)):
    prod *= int(sys.argv[i])
    i += 1

if len(sys.argv) == 1:
    print('No arguments are passed while running the program')
else:
    print('Result:', prod)
```

## Functions

- A function is a group of statements which perform a certain task.
- Function can be of two type - in-built functions [i.e. input(), print()] and user defined functions.
- User defined functions are used to process data, perform mathematical calculations and so on.
- Advantages of functions are:
  - Reusability: Once we define a function and the statements inside it those statements need not be repeated at any other place in our application, we can simply invoke or call the function and that particular logic will happen for us.
  - Modularity: When we are working on a huge application we need not put the entire code in one single script of function. We can define multiple functions which will make our application modular.
  - Maintenance: The modularity brings in easy maintenance. If an issue causes in a function or two we can easily find it out and fix then, or if we want to add something new we can just go to a particular function where the change needs to happen and add that functionality easily.
- Special properties or behaviors of functions in Python:
  - A function in Python can return multiple values at a shot. In this case all the values will be returned as a tuple so that they can't be modified and can be simply used.
  - A function in Python can be assigned to a variable, and then used as many no of times as we want.
  - We can have one function inside another function in Python (i.e. nesting of functions is possible). You can use this functionality when you want to break down your logic into multiple pieces and these child / inner functions are only available inside the parent function.
  - A function in Python can take another function as an argument.
  - A function in Python can return another function.
  - A function in Python can accept any variable type - string, int, list, tuple, dict and so on.
- Recursion:
  - Recursion is the process of a function calling itself.
  - While writing a recursive function the very first step is to define a base / end condition, or it will run into an infinite loop.
  - Good place to use recursion is whenever the same logic is repeating in a program.
  - Recursion is not a good candidate for everything, because recursion could be very confusing for people who are reading our program.
- Default Arguments:
  - If a function is expecting n arguments and we pass less than n arguments to that function Python interpreter will throw an error, in such cases using default arguments can prove out to be very handy.
  - We can pass in and set default (argument) values for any types.
  - As soon as you pass in a parameter automatically its value will be used, i.e. the default value will not be used.
- Variable / Optional Arguments:
  - When we don't know the exact number of parameters that a function should accommodate at the time of defining the function, optional arguments can prove out to be very handy.
  - If we name the optional positional argument *args, all extra positional parameters passed into the function will be stored into 'args' as a tuple
  - Name of the optional positional argument can be anything i.e. *args, *pos_params etc, ultimately it's the * which matters.
  - If we name the optional keyword argument **kwargs, all extra keyword parameters passed into the function will be stored into 'kwargs' as a dict.
  - Name of the optional keyword argument can be anything i.e. **kwargs, **key_params etc, ultimately it's the ** which matters.
  - We can pass the optional positional and keyword arguments to other functions and can alter them in between.
  

```python
# program: create a function to find the average of two numbers
def average(num1, num2):
    print('Average of two numbers:', (num1 + num2) / 2)

average(10, 20)                                 # Average of two numbers: 15.0
```

```python
# program: returning the result from a function
def average(num1, num2):
    return (num1 + num2) / 2

result = average(10, 20)
print('Average of two numbers:', result)        # Average of two numbers: 15.0
```

```python
# program: returning multiple values from a function
def calc(num1, num2):
    a = num1 + num2
    b = num1 - num2
    c = num1 * num2
    d = num1 / num2
    return a, b, c, d

# printing the tuple
result = calc(10, 5)
print(result)                                   # (15, 5, 50, 2.0)

# accessing each value from the tuple
for i in result:
    print(i, end=' ')                           # 15 5 50 2.0
```

```python
# program: showcase the use and scope of global and local variables in Python
# global variable
x = 123

def display():
    # local variable
    y = 678
    print(x)
    print(y)

print(x)                                        # 123
# print(y)                                      # NameError: name 'y' is not defined
display()                                       # 123
                                                # 678
```

```python
# program: demonstrate that local variable scope takes precedence over global variable scope
# global variable
x = 123

def display():
    # local variable
    x = 678
    print(x)

print(x)                                        # 123
display()                                       # 678
```

```python
# program: accessing global variable with the same name inside the function
x = 123

def display():
    x = 678
    print(x)

    print(globals()['x'])
    globals()['x'] = 999

print(x)                                        # 123
display()                                       # 678
                                                # 123
print(x)                                        # 999
```

```python
# program: assigning a Python function to a variable
def func_with_a_very_long_name():
    print('I am function with a very long name')

# assigning function to a variable
short_func = func_with_a_very_long_name

# invoking the function variable
short_func()                                    # I am function with a very long name
short_func()                                    # I am function with a very long name
```

```python
# program: demonstrate nesting function inside another function
def display(name):
    def message():
        return 'Hello '
    
    result = message() + name
    return result

# message()                                     # NameError: name 'message' is not define
print(display('Arnold'))                        # Hello Arnold
```

```python
# program: demonstrate passing of one function as a parameter to another function
def display(func):
    # return 'Hello ' and what ever the other function returns
    return 'Hello ' + func()

def name():
    return 'Bob'

# DON'T USE: print(display(name())) -> this way it invoke name() function and pass the value 'Bob' returned by it (i.e. we will be passing the variable and not the actual function)
print(display(name))                          # Hello Bob
```

```python
# program: demonstrate returning a function from another function
def display():
    def message():
        return 'Hello '
    
    # DON'T USE: return message() -> this way it will be returning the value which is returned after invoking message() function (i.e. we will be returning 'Hello ' and not the actual function)
    return message

# one way
func = display()
print(func() + ' Charlie')                      # Hello Charlie

# second way
print(display()(), 'Charlie')                   # Hello Charlie
```

```python
# program: passing any variable type to a function
def print_list(lst):
    for i in lst:
        print(i, end=' ')

print_list([10, 20, 30, 40])                    # 10 20 30 40
```

```python
# program: find the factorial of a number using recursion
def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n - 1)
    return result

print(factorial(5))                             # 120
```

```python
# program: demonstrate the use of keyword arguments in Python
def display(a, b):
    print(a, b)

display(a=10, b=20)                             # 10 20
display(b=10, a=20)                             # 20 10
```

```python
# program: demonstrate the use of default arguments in Python
def sum(a=0, b=0):
    print('a =', a, 'b =', b)
    return a + b

print('sum =', sum())                           # a = 0 b = 0
                                                # sum = 0
print('sum =', sum(10))                         # a = 10 b = 0
                                                # sum = 10
print('sum =', sum(b=10))                       # a = 0 b = 10
                                                # sum = 10
print('sum =', sum(10, 20))                     # a = 10 b = 20
                                                # sum = 30
print('sum =', sum(b=20, a=30))                 # a = 30 b = 20
                                                # sum = 50
```

```python
# program: demonstrate the use of variable arguments or optional arguments in a Python program
# *args is the optional positional argument in func1() which can accept any number of positional parameters
# **kwargs is the optional keyword argument in func1() which can accept any number of keyword parameters
def func1(x, *args, **kwargs):
    print('x =', x)
    print('extra positional params =', args)
    print('extra keyword params =', kwargs)

# func1()                                       # TypeError: func1() missing 1 required positional argument: 'x'
func1(10)                                       # x = 10
                                                # extra positional params = ()
                                                # extra keyword params = {}
func1(10, 20)                                   # x = 10
                                                # extra positional params = (20,)
                                                # extra keyword params = {}
func1(10, 20, 'abc', 30.5)                      # x = 10
                                                # extra positional params = (20, 'abc', 30.5)
                                                # extra keyword params = {}
func1(10, 20, 'abc', 30.5, name='David', id=7)  # x = 10
                                                # extra positional params = (20, 'abc', 30.5)
                                                # extra keyword params = {'name': 'David', 'id': 7}
```

```python
# program: demonstrate passing optional arguments to other functions
def func1(x, *args, **kwargs):
    print('from func1()')
    print('x =', x)
    print('extra positional params =', args)
    print('extra keyword params =', kwargs)

    # adding another positional parameter into tuple 'args'
    modified_args = args + (77.5, )

    # adding another keyword parameter into the dict 'kwargs'
    kwargs['id'] = 4

    func2(*modified_args, **kwargs)

def func2(*args, **kwargs):
    print('from func2()')
    print('extra positional params =', args)
    print('extra keyword params =', kwargs)

func1(10, 20, 'abc', name='Erik', sal=50.5)     # from func1()
                                                # x = 10
                                                # extra positional params = (20, 'abc')
                                                # extra keyword params = {'name': 'Erik', 'sal': 50.5}
                                                # from func2()
                                                # extra positional params = (20, 'abc', 77.5)
                                                # extra keyword params = {'name': 'Erik', 'sal': 50.5, 'id': 4}
```

## Lambdas

- A lambda is a anonymous function that will not have any name.
- Syntax: lambda \<argument-list\>: \<expression\>
- Unlike a function a lambda will always return a function back.
- It is not a good practice to use it all the times by assigning it to a function and invoking it, but lambda expression are very helpful when it use them inside other functions like map, filter and reduce. These functions will take a function as a list as parameter and will apply that function to every element in that list.
- You can't write multiple lines lambda in Python, lambda functions can only have one expression.

```python
# program: print the cube of a number using lambda expression
def cube(n):
    return n ** 3

lambda_cube = lambda n: n ** 3

print(cube(2))                                  # 8
print(lambda_cube(3))                           # 27
```

```python
# program: print YES if the number is even, NO if the number is odd using lambda expression
is_even = lambda n: 'YES' if n % 2 == 0 else 'NO'

print(is_even(10))                              # YES
print(is_even(9))                               # NO
```

```python
# program: print the sum of two numbers using lambda expression
calc_sum = lambda a, b: a + b

print(calc_sum(4, 5))                           # 9
```

```python
# program: retrieve and print all the even numbers from a given list of numbers using filter() function with lambda expression
lst = [10, 21, 9, 33, 48, 95, 10, 74]

# even numbers without lambda expression (process 1)
def is_even1(n):
    if n % 2 == 0:
        return True
    else:
        return False

filtered_list = filter(is_even1, lst)
print(filtered_list)                            # <filter object at 0x10bf94ee0>
print(type(filtered_list))                      # <class 'filter'>
even_nos_list1 = list(filtered_list)
print(even_nos_list1)                           # [10, 48, 10, 74]

# even numbers without lambda expression (process 2)
def is_even2(n):
    if n % 2 == 0:
        # The return value should a truthy value i.e. any of the following statements will work
        # return True
        # return 9999
        # return 1.10
        # return 'YES'
        return -1

even_nos_list2 = list(filter(is_even2, lst))
print(even_nos_list2)                           # [10, 48, 10, 74]

# even numbers with lambda expression
even_nos_list3 = list(filter(lambda n: n % 2 == 0, lst))
print(even_nos_list3)                           # [10, 48, 10, 74]
```

```python
# program: double all the numbers present in a list and print them using map() function and lambda expression
lst = [2, 3, 4, 5, 6]

# double the numbers without lambda expression
def double(n):
    return n * 2

mapped_list = map(double, lst)
print(mapped_list)                              # <map object at 0x108754ee0>
print(type(mapped_list))                        # <class 'map'>
doubled_list1 = list(mapped_list)
print(doubled_list1)                            # [4, 6, 8, 10, 12]

# double the numbers using lambda expression
doubled_list2 = list(map(lambda n: n * 2, lst))
print(doubled_list2)                            # [4, 6, 8, 10, 12]

```

```python
# program: find the sum of all the elements present in a list using reduce() function and lambda expression
from functools import reduce

lst = [1, 2, 6, 8, 4, 7]

# summation without lambda expression
def sum(x, y):
    return x + y

reduced_list = reduce(sum, lst)
print(reduced_list)                             # 28
print(type(reduced_list))                       # <class 'int'>

# summation with lambda expression
summation = reduce(lambda x, y: x + y, lst)
print(summation)                                # 28
```

## Decorators and Generators

- Decorators:
  - A decorator is a function that performs additional logic on a given function (i.e. it takes a function as input).
  - A decorator also returns a function back as the result.
  - If we always want to apply a particular decorator to a function we can do that using @\<decorator-function-name\>
  - We can also do decorator chaining in Python. In such case, the decorator name that we will mention right on top of the function (closest to that function) will be applied first and then the output of that decorator will be passed to the other decorator function that is present on top of it.
- Generators:
  - Generators are functions that return a sequence of values back.
  - A generator function is used just like any other function but it uses a 'yield' statement.
  - As we generate our custom sequence using the 'yield' we will be storing each values in that sequence and at the end of the function or at the end of the sequence generation we will return the entire sequence back.
  - A generator function is very similar to the range data type, but in this case you can come up with your own custom sequences like generation of random numbers or a sequence which is very specific to your application.

```python
# program: double the number returned by another function using a decorator function
def decor(func):
    def inner():
        result = func()
        return result * 2
    return inner

def num():
    return 5

result_func = decor(num)
print(result_func())                            # 10
print(decor(num)())                             # 10
```

```python
# program: double the number returned by another function using a decorator function using @<decorator-function-name>
def decor(func):
    def inner():
        result = func()
        return result * 2
    return inner

@decor
def num():
    return 5

print(num())                                    # 10
```

```python
# program: demonstrate applying decorators on a method that returns a string
def decorfunc(func):
    def inner(nm):
        return func(nm) + '! how are you?'
    return inner

@decorfunc
def say_hello(name):
    return 'Hello ' + name

print(say_hello('Steven'))                      # Hello Steven! how are you?
```

```python
# program: demonstrate the use of decorator chaining in python
def square(func):
    def inner():
        result = func()
        return result ** 2
    return inner

def half(func):
    def inner():
        result = func()
        return result / 2
    return inner

@square
@half
def num1():
    return 10

@half
@square
def num2():
    return 10

print(num1())                                   # 25.0
print(num2())                                   # 50.0
```

```python
# program: create a custom sequence which has all the multiples of 5 from 1 to 100 using a generator function
def custom_range_gen(x, y):
    while x <= y:
        if x % 5 == 0:
            yield x
        x += 1
    
gen_seq = custom_range_gen(1, 100)
print(gen_seq)                                  # <generator object custom_range_gen at 0x110dea6d0>
print(type(gen_seq))                            # <class 'generator'>
lst = list(gen_seq)
print(lst)                                      # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
```


