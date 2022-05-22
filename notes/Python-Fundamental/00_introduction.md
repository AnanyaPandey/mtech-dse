### Prof Parthasarthy 
# Intro to Python for data science
### DSECLPFDS
Life is an amalgamation of various facets and as an individual we all aim to experience life to its fullest ...

Pre requisite : 
* Be mentally present, ovserve and listen.
* Solve exercises regularly.
* Do an extra bit of learning 

### Course Objective : 
* Fundamental programming
* data problems in python
* create graphs and explore data
* Bridge course for totally new to python
* NOT : comprehensive in depth discussion/OOPS
* NOT : not about python packages/libraries tools

Books : 
* Python for everybody
* Python Data Science handbook

## Introduction 
A comp program is a set of instruction that run in a sequence. For any program a computer needs a compiler or interpreter to translate it to the machine friendly language. Python overtook java as most used language in many scenarios! Python is interpreted language ; meaning it will run till it finds the error, rather than not at all running if there is error.

Python has been used for many years but recently its is picked up have a great active community, english like language not many contraints. Highly readable, Most fond for data science. simple design and easy to learn. Python is also open source.

Python can be used for pretty much anything any language is used for 
1. Web development
2. Data science
3. Mathematical analysis
4. Software development 
5. Scripting.
6. Systme admin and automation. 
7. GUI development

Python Ecosystem : 
* Core Python
* Distribution
* Frameworks
* Third party library

Python IDE : 
An IDE, or Integrated Development Environment, enables programmers to consolidate the different aspects of writing a computer program. IDEs increase programmer productivity by combining common activities of writing software into a single application: editing source code, building executables, and debugging.

How to install Jupyter : 
https://test-jupyter.readthedocs.io/en/latest/install.html

Data types : 
Int 
String
tuple
Sets
.. are immutable 

list 
dictionary 
.. are mutable 

### Parsing through the string

```python
stl = "string for learning"
fml = "This is string for my learning"
stl[5]
stl[-1] # depicts the last character of the string

stl[4:7] # returns character from 4 to 6
stl[-2:-4] # negative indexing also works similarly

```
### built in functions for strings. 

```python
stl.upper() # returns the string in upper case
stl.isupper() # returns whether the string is upper case or not 
stl.isnumric() 
dir(str) # retuens all possible methods and functions for str

```
### Stripping and slicing of a string 

```python
stl.rstrip() # all right side space is stripped
stl.lstrip()
stl.strip()
# These methods does not store it in the string they just return the output.

fml = "This is string for my learning **** " # We want to remove *** "
fml.rstrip(' * ')

line = "rahul 29 40 35"
splitted = line.split()
print(splitted)
['rahul', '29', '40', '35']

line = "rahul,29,40,35"
splitted = line.split(",")

```
### Lets find the character or string within string 

```python
line.find('rahul')
line.replace("ra","me")
'mehul,29,40,35'

```

### Tuple and opertions

Tuples are tricky if not used in proper format. 

```python
mtup = (1,2,"hello",True)
type(mtup)
tuple
len(mtup)
4
mtup[1]
2
mtup[-1]
True
type(mtup[-1])
bool

tup1 = (1,2,3,4)
tup2 = (5,6,7,8)
tup1 + tup2 

# Understand immutability
tup1[2] = 30 
TypeError: 'tuple' object does not support item assignment

# we cannot change since it is immutable.
tup1.append(2,4)
AttributeError: 'tuple' object has no attribute 'append'
temptup = (2,4)
tup1+temptup
(1, 2, 3, 4, 2, 4)

```

# List and operations 
Creating, operating, appending, etc. 

```python
myl = []
myl = [1,2,3,"rahul",True]
len(myl) # returns the length of list 
myl[2]
myl[-2]
myl[3:5]
myl[:3]
myl[:]

myl.append(200)
[1, 2, 3, 'rahul', True, 200]

myl[1]  = "Two"
myl
[1, 'Two', 3, 'rahul', True, 200]

myl.append([2,3,4])
[1, 'Two', 3, 'rahul', True, 200, [2, 3, 4]]
# Added list as an element.

# Now we want that only as list elements separately not as one element
myl.extend([5,6,7])
[1, 'Two', 3, 'rahul', True, 200, [2, 3, 4], 5, 6, 7]

# Adding somethingin between - insert
myl.insert(4,"Ram") # at 4th index insert Ram
[1, 'Two', 3, 'rahul', 'Ram', True, 200, [2, 3, 4], 5, 6, 7]

myl[4] = "Raam"
[1, 'Two', 3, 'rahul', 'Raam', True, 200, [2, 3, 4], 5, 6, 7]

myl.remove("Two")
[1, 3, 'rahul', 'Raam', True, 200, [2, 3, 4], 5, 6, 7]

nmbr = [1,2,3,4,5,6,7,8]
sum(nmbr)
min(nmbr)
max(nmbr)
nmbr.sort()
nmbr.sort(reverse = True)

```

### Sets and operations 

```python
mtset = {}
mset = {1,2,3,4,5,6,6,7,8,9}
{1, 2, 3, 4, 5, 6, 7, 8, 9}
# duplicate numbers are not repeated and these are homogenous

settest = set(myl)
settest

mset.add(20)
mset.pop(3)
mset.remove(20)
mset.sort() 

# Other opetions include 
# union
# intersection
# difference 

```

# Dictionary 

```python
mydict = { 1:"rajnish", 2:"Rambo"}
print(my_dict)

mydict.keys()
dict_keys([1, 2])
mydict.values()
dict_values(['rajnish', 'Rambo'])

mydict[1]
'rajnish'

mydict.get(2)
'Rambo'

mydict[1] = 34
{1: 34, 2: 'Rambo'}

# in order to loop
# for key in mydict.keys() :
# for val in mydict.values() : 

same keys not possible since it will be overwritten
dictt = {11:'hi', 11:'bye'}
{11: 'bye'}
```


# Operators 

* Arithmetic : + - * // % ** / 
* Bitwise & | ^ 
* Logical and or not
* Comparison == != <> > < <= >= 
* Assignment = += -= *= /= %= **= 
* membership/identity in not in /is not is


```python
myl = [1,2,3,4,5]
1 in myl
True 

10 in myl 
False

a = 100
b = 50

a is a 
True

a is 100 
True

# is operator is used ot check if they have the same id 

a is b 
True 

# Because their addresses are same 

>>> id(a)
140721225891168
>>> id(b)
140721225891168
>>>

# if it is same values python points it to same memory location.
```
