# 01_Introduction
## Lecture 3 18-apr-2021
#### Topics covered :

1. Conditions and Loops
2. Exception
3. File Handlng

## Condition Statement 

To check one or multiple conditions and make the program act accordingly.

```python
name = "tiger"
if name == "tiger" :
    print("Tiger found")
else :
    print("Tiger not found search again")
```
We can add multiple conditions using logical operator and multiple ifs

```python
forest = ['tiger','monkey','zebra','cat']
name = 'tiger'
if name in forest : 
    print("animal found")

percent = 88.7
if percent < 60 and percent > 45 :
    print("Second division")
else if percent < 33 :
    print("Not Sure")
else if percent > 80 :
    print("Distinction")
```

## Exception Handling

```python
try : 
    num = input("Enter a number")
    if num > 5 :
        print("Something")
    else : 
        print("Something else")

except Exception as e:
    print(e)
    print("Looks like something goofy happend")
print("I will be printed for sure")
```

## Looping 
Two most used loops are while and for

```python
i = 0 
while i < 5 :
    print(i)
    i+=1
print("outside loop")

# Computing average 
mark_list = [10,20,10,14,25,12,14]
tot_marks = 0 
stu_count = len(mark_list)
print("num of students",stu_count)
i = 0
while i < stu_count :
    tot_marks = tot_marks + mark_list[i]
    i+=1
print("Total marks :",tot_marks)
print("Average : "tot_marks/stu_count)

# Break Statement to come out of loop
i = 0 
while i < 10 :
    print(i)
    i+=1
    if i == 6 :
    break
print("out of loop)

# Continue : Continue skips the current loop and continues with the loop

listt = [1,2,3,4,5,6,6,7]
num = int(input("enter a number"))
i=0
while i < len(listt):
    if num == listt[i] :
        print("number present")
        break
    index+=1 
print("outside loop")

```
### For loop 

```python
# for i in range()
# for i in list
# for i in dict.keys()

for i in range(5):
    print(i)

# for i in range(start,stop,step)
for i in range(2,10,2) :
    print(i)
```

### Functions : 

Repeated works can be saved and reused later through functions.

```python
def comp-average(list-num):
    count = len(list-num)
    i,total = 0,0

    for i in list-num :
        total = total + i 
    avg = total / count
    return(avg)

list-num = [1,3,3,5,6,7,8,4,3,1,1]
print("The average is ",comp-average(list-num))

# def Funcname() : No argument
# def Funcname(defargumentval=10) : 
```

#### Arguments and parameters in functions 

When a function is called the passed variables are called arguments. When function is defined those are called parameters. Both are same and can be used interchangeably.

```python
def fname(sente,time):
    for i in range(time):
        print(sente, end = ",")  # to print in the same line use the end = comma. 

def fname(sente,time=5):
    for i in range(time):
        print(sente)

fname("@",10)
fname("@")

# Default argument sequence has to be maintained and cannot be shifted.
```

### Factorial 

```python
import math
math.factorial(5)

# Using For loop
def factoria(num):
    factorial = 1
    # check if the number is negative, positive or zer
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1) :
            factorial = factorial*i
        print("The factorial of",num,"is",factorial)

factoria(5)
factoria(6)

```

### File Handling 

1. Opening a file 
2. Read a file 
3. Closing a file 

```python
f = open("test.py")
content = f.read()
print(content)
f.close

```


### Data processing of a file 

```python
file = open("dummyfile.txt")
content = file.read()
lines = content.split("\n")
print(lines)
print(type(lines))
# Each line acts as a list, a lists of strings.

for eachline in lines :
    print(index,",",lines) # This will do the numbering. and prints each line. 
    
    print("\t Num of characters",len(eachline))
    words = eachline.split()
    
    print("\t Num of words",len(words))
    index+=1
```
#### Exceptions with files 

```python
try : 
    file = open("hello.txt")
    file.read()
    file.close()

except :
    print("Something is wrong")
```

### Writing to a file 

```python
# opening a file is required so tht we can handle it, be it read or write
# "w" will create a file for you to edit. 

f = open("new-nonexisting-file.txt"."w")
print("Some text",file=f )
print("New text",file=f )
print("SomeMore text",file=f )
print("New More text",file=f )
f.close()

# We can open the file in same manner.

# Directly writing to the file
fout = open("someother.txt","w")
fout.write(" This is a new text \n")
fout.write(" This is a another new text \n")
fout.close()

# fout = open("someother.txt","w") w will just overwrite it 
fout = open("someother.txt","a") # This will add /append to the file 
fout.write(" This is a New student text \n")
fout.write(" This is a latest text \n")
fout.close()
```
####  End of File 