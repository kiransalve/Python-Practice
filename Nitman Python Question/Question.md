# List vs Tuple

In Python, both List and Tuple are ordered collections used to store multiple items, but the main difference is mutability.

List is mutable, meaning elements can be modified after creation.

Tuple is immutable, meaning elements cannot be changed once created

List consume more memory that tuple

List is slower than tuple

List creation - [] and tubele creation - ()

# What is Decorator?

A Decorator is just a function that takes another function as an argument, add some kind of
functionality and then returns another function without changing its actual code.

We use it for logging, authentication, timing execution, validation etc.

# Difference between List and Dictionary 

List stores items using index positions.

Dictionary stores data using key–value pairs.

List is created by [] and dictionary is created by {}

List can allow duplicate value, In dictionary key must be unique

# How Memory Managed In Python?

Python manages memory automatically using private heap space, reference counting, and garbage collection to free unused objects


# Difference Between Generators and Iterators

Both generators and iterators are used to iterate over a sequence of values one at a time

Generators

Generators are iterators which can execute only once.

Generator uses “yield” keyword.

Generators are mostly used in loops to generate an iterator by returning all the values in the loop without affecting the iteration of the loop.

Every generator is an iterator.

```
EXAMPLE:

def sqr(n):
    for i in range(1, n+1):
    yield i*i
a = sqr(3)

print(next(a))
print(next(a))
print(next(a))

Output:
1
49

```

Iterator

An iterator is an object which contains a countable number of values and it is used to iterate over iterable objects like list, tuples, sets, etc.

Iterators are used mostly to iterate or convert other objects to an iterator using iter() function.

Iterator uses iter() and next() functions.

Every iterator is not a generator.

Example:

```
iter_list = iter(['A', 'B', 'C'])

print(next(iter_list))
print(next(iter_list))
print(next(iter_list))

Output:
ABC

```
