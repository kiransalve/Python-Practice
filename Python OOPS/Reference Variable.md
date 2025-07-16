A reference variable is a variable that refers to (or "points to") the memory location where an object is stored — not the object itself.

A reference variable is just a name for an object stored in memory.

a = [1, 2, 3]

b = a

a is a reference to the list [1, 2, 3]

b = a means: b is now another reference to the same list

In Python, variables don't store the actual object — they store a reference (a pointer) to the object.

