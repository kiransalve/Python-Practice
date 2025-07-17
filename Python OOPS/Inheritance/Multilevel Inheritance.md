Multilevel Inheritance means:

A child class is derived from a parent class, which is also derived from grandparent class.

In simple words:

Grandparent → Parent → Child

```text
class Grandparent:
    def show_grandparent(self):
        print("I am Grandparent")

class Parent(Grandparent):
    def show_parent(self):
        print("I am Parent")

class Child(Parent):
    def show_child(self):
        print("I am Child")

# Creating object of Child class
obj = Child()
obj.show_grandparent()  # from Grandparent
obj.show_parent()       # from Parent
obj.show_child()        # from Child



+------------------+
|   Grandparent    |
+------------------+
          ↓
+------------------+
|     Parent       |
+------------------+
          ↓
+------------------+
|      Child       |
+------------------+

```

Key Points:

Child class inherits from Parent.

Parent class inherits from Grandparent.

So, Child class has access to both Parent and Grandparent methods.



```text

class Employee:
    def __init__(self, name):
        self.name = name

    def show_employee(self):
        print(f"Employee Name: {self.name}")

class Manager(Employee):
    def __init__(self, name, team_size):
        super().__init__(name)
        self.team_size = team_size

    def show_manager(self):
        print(f"Manager of {self.team_size} people")

class Director(Manager):
    def __init__(self, name, team_size, budget):
        super().__init__(name, team_size)
        self.budget = budget

    def show_director(self):
        print(f"Director with budget: ₹{self.budget} Cr")

boss = Director("Kiran", 10, 5)
boss.show_employee()   # from Employee
boss.show_manager()    # from Manager
boss.show_director()   # from Director

Output

Employee Name: Kiran
Manager of 10 people
Director with budget: ₹5 Cr

```


```text
+------------------------+
|       Employee         |  ← Base class
|  - name                |
|  + show_employee()     |
+------------------------+
            ↓
+------------------------+
|        Manager         |  ← Intermediate class
|  - team_size           |
|  + show_manager()      |
+------------------------+
            ↓
+------------------------+
|        Director        |  ← Derived class
|  - budget              |
|  + show_director()     |
+------------------------+

```


