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
