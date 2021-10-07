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

### Sequence Type - list

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

### list vs tuple

- List uses square brackets to wrap a list of elements, whereas tuple uses parenthesis.
- For a list using square brackets are mandatory, whereas for a tuple its optional to use a pair of parenthesis.
- List is mutable, whereas tuple is immutable.
- List should be used in situations where we need to do manipulations on the elements, tuple should be used where consistency of the elements are mandatory.
- A list cannot be used as a key to the dictionary, because a dictionary key should be hashable and immutable, since tuple is immutable we can use tuple as a key to the dictionary.

### Set Types - set and frozenset

- The set sequence type does not allow duplicates.
- Set does not maintain any order of its elements.
- We cannot perform indexing, slicing or repetition on a set.
- A frozenset does not allow add, update or remove operation in a set.
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

```python
# syntax: range(<start_value>, end_value, <step>)
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
