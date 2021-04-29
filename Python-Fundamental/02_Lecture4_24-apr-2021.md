## Lecture 4
### Quick Revision : 

### Agenda : 

* Scipy
* Numpy
* Pandas
* Data Exploration
* Matplotlib
* Seaborn
* Sckit-Learn

## Scipy Ecosystem : 
Consisting of libraries, including mathematics, science, engineering and data analysis and so on. Data could be numerical or textual imaage sound of any format. 

### Numpy : Numerical python
python library for working with arrays. It is helpful working with matrics, algebra, fourier etc.
Numpy helps in solving problems 50x faster than conventional dta structures in python. Data manipulation and analysis requires heavy computing and thus we need faster/less memory requirement of array. Object created by numpy is ndarray. numpy array is homogenous multidimensional array. 
Python arrays are different from numpy arrays. 

### Handson on : Operations on arrays.

```python
import array 
myarray = array.array('i',[1,2,3,4,5])
#array('i', [1, 2, 3, 4, 5])
 type(myarray)
#<class 'array.array'>
```

### Numpy arrays : 

```python
import numpy as np
ar = np.array([1,2,3,4,5,6])
# Inside array we can pass a list or set but should be homogenous
type(ar)
#<class 'numpy.ndarray'>

arr = np.array((1,2,3,4,5)) # we passed tuple
zero_arr = np.array([1]) # This is a zero dimensional array (a single element array)
oned_arr = np.array((1,2,3,4,5)) # an array is simply 1 d array
twod_arr = np.array([[1,2],[3,4],[4,5]]) # Two dimensional array like matrix.

floatlist = [1.3,2.5,6.4,2.4,8.7]
npfloatlist = np.array(floatlist)

# If we try to mix the different type of data it will make it one type
# e.g. : if we use int and string : it will convert everything to string.
# if we take int and float it will conver everything to float.
# While creting if we specify the type it will give array

lst = [1,2,3,'a']
nlst = np.array(lst, dtype =int)
```

### Backwards conversion

```python
arr = np.array((1,2,3,4,5,6))
arr.tolist()
# Check other conversions
```

### Properties of numpy array

```python
type(np.array) # returns numpy array
# if we wnat to know the data type of the data inseide array
arr = np.array([1,2,3,4])
arr.dtype
arr.ndim # Returns the dimension of the array
arr.shape # dimension, row x col
arr.size # number of elements 
```


### Prepopulated Arrays :

```python
np.zeros(6)
#array([0., 0., 0., 0., 0., 0.])

np.zeros(5, dtype=int)
np.ones(5)
np.empty(10) # creates empty array keeping space for 10 elements

np.empty(5)
array([1.12516428e-311, 1.12516428e-311, 1.12516428e-311, 1.12516428e-311,
       0.00000000e+000])
# It retruned whatever is there at the memory location

np.arange(1,10) # Creates a range from 1 to 9 NOT 10.
np.arange(5,50,5) # start stop and step 
```

### 2D Arays 

```python
l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]

twod = np.array([l1,l2,l3])
twod.shape
twod.size
```

### Numpy array computation and opertions 

```python
# Indexing on arrays
# Array indexing is same as list indexing 
twod[2,2] # 3rd row and 3rd col 
twod[2,2] = 242 # np arrays are mutable 

# Creating sub array 
arra = np.array([1,2,3,55,4,3])
asub = arra[:3]
asub[0] = 11
print(arra)
[11  2  3 55  4  3]
print(asub)
[11  2  3]
arra.view() # printing will take mem location view will not.

# So Python keeps the mem location same 
# In order to keep it unaffacted we use copy

asub = arra[:3].copy
# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

```

### Reshaping 

```python
arra = np.array([1,2,3,55,4,3])
areshaed = arra.reshape(2,3)
areshaed.view()
array([[ 1,  2,  3],
       [55,  4,  3]])

# The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
```

### Arithmetic operations : 

```python
arra = np.array([1,2,3,55,4,3])
sum(arra)
68

# Creating random intiger
a1 = np.random.randint(1,100,size=1000)
# 1000 elements, between 1 and 100 

%timeit # calculate time for any operation

%timeit sum(arra)
%timeit np.sum(arra)

# in sum() it does type checking of data. 
arra + 5 # Singular arithmetic applies adding to all elements
arra**2 # Singular  arithmetic applies adding to all elements
arra.add(5) # Same as above.

print(arra)
array([[1, 2, 3],
       [4, 5, 6]])

np.sum(arra,axis=0) # Axis = 0 means row wise addition.
array([5, 7, 9])

np.sum(arra,axis=1) # Axis = 1 means column wise addition
array([ 6, 15])

# This row and column wise operation to axis 0 and axis 1 will remain for all 2D data structures in python

# Comparison 
arra == 3
array([False, False, True, False, False, False])

# it sums all True, consider True = 1 and False = 0
np.sum(arra < 55) # HOW MANY!!!  elements are less than 55
6 # all 6 elements are less than 55

#Another method 
np.greater(arra,55) # check how many greater than 55

# Checking min and max 
arra.mean()
arra.std()
arra.min()
arra.max()
np.max(arra,axis=0)

# any and all 

np.any(arra > 100) # Returns True if any element in array is > 100
np.any( (arra<5) | (arra >100)) 

np.all([[True,False],[True,True]]) # if everything is True then only True
# Test whether all array elements along a given axis evaluate to True.
```

### Linear Algebra 

```python
x = np.array([[1,2],[3,4]])
print(x)

x.transpose() # Transposes the array 
np.eye(10) # Returns the identity matrix array of size 2D 10

# 20x + 10y = 350
# 17x + 22y = 500

# Ax = B 
A = np.array([[20,10],[17,22]])
B = np.array([350,500])
X = np.linalg.solve(A,B) # X is an np array of 2 elements x and y 
# X is a matrix/array of two elements x1 and x2

# Reference for Linear  ALgebra :  np.linalg
```

## Lecture - 5
### 11:30 - 13:00

## Pandas
A python library very useful while working with datasets. Data clearning, manipulation, analysis etc. 
Help us clean and transform messy data. Also allows us to handle empty data, wrong/null values. 

### Dataframe : 
A data frame is a datastructure 2D where data is mentioned in row and columns. It allows python to perform data operations across these data frames. from importing, operating exporting it allows pretty much everything. 

![](Capture1.jpg)

### Operations : 
 * Importing
 * Series cration
 * Dataframe Creation
 * Reading
 * Writing
 * Functions offered by pandas 

```python
import pandas as pd
import numpy as np
pd.__Version__

# Creating series 
s1 = {"one":[1,2,3,4]}
s2 = {"two":[1,2,3,4]}

data1 = pd.series(s1)

a1 = np.random.randint(5,size=5)
s1 = pd.Series(a1, index=['a','b','v','d','e']) # This is explicit indexing
# If we do not provide indexing it will take default 0 - n indexing
# Index is a series so this series can be used in pandas. 
```

### Data Frame : 

```python
dict = {
    "id":[1,2,3,4,5],
    "name":["abhi","raj","rahul","badri","salil"],
}
df = pd.DataFrame(dict)

type(df)
<class 'pandas.core.frame.DataFrame'>

df.columns
Index(['id', 'name'], dtype='object')

df.dtypes # Returns the type of the individual columns 
id       int64
name    object
dtype: object

### Now we create series and merge then into a dataframe
s1 = pd.Series([1,2,3,4,5], name="id")
s2 = pd.Series([100,20,200,180,50], name="salary")
s3 = pd.Series([True,True,False,False,False], name="working")

df2 = pd.DataFrame([s1,s2,s3])
df2.T

   id  salary  working
0   1     100        1
1   2      20        1
2   3     200        0
3   4     180        0
4   5      50        1
```

## More Practical Approach


```python
# Picking up the file student in csv, json, sql, excel
student = pd.read_csv("student.csv")
stu2 = pd.read_excel("student2.xlsx",)

student.to_csv("myfirstcsv.csv")
stu2 = to_excel("my-student2.xlsx",)
```

# Data Selection or Slicing 

```python
name = df["COl-name"] # Returns enture series 
listofcol = ["name","id","dob"]
extracteddata = df[listofcol]
# df.columnname = works fine 

# iloc and loc 
df.iloc[0] # Returns all columns for first row 
df.iloc[:3] # first 3 rows of all columns entire data
df.loc[["id","name"]] 
# Name of column
```
### slicing with conditioning

```python
df[df.Colname > 3]
df.[df.quiz > 33]
df[(df.salary <= 33>) | (df.workex > 7)]

## Same thing can be done through query 
df.query('quiz > 33')
```

### Data Exploration 
#### Task in hand 

* import data
* how the data looks 
* Clean the Data
* Group Merge
* Export result
* Explore Visualize

```python
bikes = pd.read_csv("filename.csv")
bikes.head()
bikes.info() # What columns of what types, null count, etc.

bikes.shape
bikes.columns # Each column is a series
bikes.dtypes

# Return the unique values 
bikes.instant.unique() # this col is like index
bikes.dteday.unique()
bikes.season.unique()
bikes.season.duplicated().sum() # checking for duplicates 

# Are thre any Null values 
np.sum(bikes.isnull())
bikes.isnull().sum()
bikes.isna().sum()

bikes.dropna() # Dropna drops the rows with na or blank columns and displays 
bikes.dropna(inplace=True) # make permanent change

# if there are duplicates in data, bikes, col : instant, drop them in place permanently. 
bikes.drop_duplicates(subset = "instant", inplace=True) 

#We can also replace na values with something else/ 
bikes.fillna()
df.fillna(0) # replace with 0 

datedtimes =  pd.to_datetime(bikes.dteday) # We created the date./time series from a dataframe column
bikes.year = datedtimes.dt.year # and then created new column from that
```

### Grouping and Merging in data.

```python
# need to identify how many bikes got rented in the year 2011
  bikes2011 =   bikes[bikes.year == 2011]

# How many casual users in the data 
dfbyseason = bikes.groupby("season") # Creating a grouped data. 
# This grouped data cannot be individually accessed. 

dfbyseason.casual.sum() # This will give eachseason casual user sum 

#We will now sum it to know how many total cases per season
# Creating sum for casual /OTC users. 
bikes.groupby("season").casual.sum() # OR 
seriescasual = dfbyseason["casual"].sum()

# Same for registered : 
series_registed = dfbyseason.registered.sum()
type(series_registed)


frames = pd.concat([seriescasual,series_registed], axis =1)
frames.total = frames.seriescasual + frames.series_registed # creating a column 
frames.to_csv("Seasonal-rent.csv")
```