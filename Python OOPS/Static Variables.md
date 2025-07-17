The variable which have same value for all object

a static variable is a variable that is shared across all instances of a class. It is also called a class variable.

A static variable is defined inside the class, but outside any instance methods (including __init__). It is common for all instances of the class.

You can also access static variables using self, but it's recommended to use ClassName.variable for clarity.

```text

class Counter:
    object_count = 0  # static variable

    def __init__(self):
        Counter.object_count += 1

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

print(Counter.object_count)  # 👉 3


```
