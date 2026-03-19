# 1. What is difference between list and tuple?

In Python, both List and Tuple are used to store multiple items in a single variable.
The main difference between them is mutability.

Mutability

List → Mutable (we can change, add, or remove elements after creation)

Tuple → Immutable (cannot be modified after creation)

List example -
my_list = [10, 20, 30]
my_list[1] = 50
print(my_list)

[10, 50, 30]

Here we changed the value, so list is mutable

Tuple example -
my_tuple = (10, 20, 30)
my_tuple[1] = 50


TypeError: 'tuple' object does not support item assignment


Syntax

List uses square brackets []

Tuple uses parentheses ()

Performance

Tuple is faster than List

Because tuples are immutable, Python can optimize them better.

import timeit

timeit.timeit("[1,2,3,4,5]", number=1000000)
timeit.timeit("(1,2,3,4,5)", number=1000000)

Tuple creation is slightly faster.

Memory Usage

Tuples use less memory compared to lists because they are immutable.

Use Cases

Use List when:

Data needs to change

Adding/removing items

Dynamic collections

shopping_cart = ["milk", "bread", "butter"]
shopping_cart.append("eggs")

Use Tuple when:

Data should remain constant

Protect data from modification

Used as dictionary keys

location = (19.0760, 72.8777)   # latitude, longitude

Coordinates should not change, so tuple is ideal.


Hashability

Tuple can be used as dictionary keys, but lists cannot.

Tuple as key
data = {(1,2): "Point A"}

List cannot be key
data = {[1,2]: "Point A"}   # Error

Because dictionary keys must be immutable

In short, Lists are mutable, flexible, and used when data changes, while Tuples are immutable, faster, and used when data should remain constant or needs to be used as dictionary keys.

# 2. What is decorators?

Decorators are function that takea another function as an argument, add some kinf of functionality to that and return another function without changing its actual code.

Decorators are widely used for logging, authentication, timing, caching, validation, etc.

Why Decorators Are Possible in Python

Python treats functions as first-class objects, meaning:

Functions can be passed as arguments

Functions can return other functions

Functions can be assigned to variables

This allows decorators to work.

def greet():
    print("Hello")
    
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper


Here:

func → original function

wrapper → adds extra behavior


@my_decorator
def greet():
    print("Hello")

greet = my_decorator(greet)

Before function runs
Hello
After function runs

# 3. Difference Between List Comprehension and Dictionary Comprehension?

st Comprehension

Used to create a list

Syntax: [expression for item in iterable if condition]

```
Example:

nums = [1, 2, 3, 4]
squares = [x**2 for x in nums]

# Output: [1, 4, 9, 16]

Returns a list
```

Dictionary Comprehension

Used to create a dictionary (key-value pairs)

Syntax: {key: value for item in iterable if condition}

```
Example:

nums = [1, 2, 3, 4]
square_dict = {x: x**2 for x in nums}

# Output: {1: 1, 2: 4, 3: 9, 4: 16}

Returns a dictionary
```

# 4. What is a Lambda Function?

A lambda function is a small anonymous function (function without a name) in Python.

It is used for short, one-line operations

Syntax : lambda arguments: expression

```
add = lambda a, b: a + b
print(add(2, 3))

# Output: 5

```
# 5. Difference between deep copy and shallow copy?

Shallow Copy

Creates a new object, but references same inner objects

Changes in nested objects will affect original

```
import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)

b[0][0] = 100
print(a)  # [[100, 2], [3, 4]]
```

Deep Copy

Creates a completely independent copy

Copies all nested object

```
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0][0] = 100
print(a)

# [[1, 2], [3, 4]]
```

# 5. Explain Pandas groupby with example?

Groupby is used to group data based on a column and then perform operations like sum, mean, count, etc.

```
import pandas as pd

data = {
    'Product': ['A', 'A', 'B', 'B', 'C'],
    'Sales': [100, 150, 200, 250, 300]
}

df = pd.DataFrame(data)

df.groupby('Product')['Sales'].sum()

# multiple operation
df.groupby('Product')['Sales'].agg(['sum', 'mean', 'count'])

```

# 6. How do you handle missing values in Pandas?

```
1. Detect missing values

df.isnull()        # shows True/False
df.isnull().sum()  # count of missing values

2. Drop missing values

Remove rows: df.dropna()

Remove columns: df.dropna(axis=1)

3. Fill missing values

Numerical data
Mean / Median:

df['col'].fillna(df['col'].mean(), inplace=True)

Categorical data
Mode / constant:

df['col'].fillna('Unknown', inplace=True)


4. Forward & Backward fill (very important for time-series)

df.fillna(method='ffill')  # forward fill
df.fillna(method='bfill')  # backward fill

5. Interpolation (for smooth data)

df['col'].interpolate()



```

# 6 What is NumPy?

NumPy (Numerical Python) is a Python library used for:

numerical computations

working with arrays and matrices

performing fast mathematical operations

It provides a powerful object called ndarray (n-dimensional array)


# 7. Why is NumPy faster than Python lists?

1. Homogeneous data

NumPy arrays store same data type

Python lists can store mixed types

This makes NumPy more memory-efficient

2. Contiguous memory

NumPy stores data in continuous memory blocks

Lists store references (pointers)

Faster access and computation

3. Vectorization
   
NumPy performs operations on entire array at once

No need for loops


4. Written in C

NumPy operations are implemented in C language

Python lists run in slower Python loops

# 8. Find second largest number in list?

```
nums = [10, 20, 4, 45, 99]

first = second = float('-inf')

for num in nums:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print(second)
```
