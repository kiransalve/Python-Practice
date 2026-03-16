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

