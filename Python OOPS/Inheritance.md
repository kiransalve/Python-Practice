Inheritance means a class (child) can use the properties and methods of another class (parent).

```text

# Parent Class
class Animal:
    def __init__(self):
        self.alive = True

    def eat(self):
        print("This animal eats food.")

# Child Class
class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("The dog barks.")

# Create object of Dog
tommy = Dog()

# Accessing parent class method
tommy.eat()     # Output: This animal eats food.

# Accessing child class method
tommy.bark()    # Output: The dog barks.

```

Key 

1. Child can take the data and methods from parents but parents can not take from child
2. Child can inherite - Data members, methods, constructor
3. Child can not inheritate the private variable and methods
   

Conditions

If child class have not any constructor then when we create object, the parents class constructor will be called

```text

class Parent:
    def __init__(self):
        print("Parent class constructor called")

class Child(Parent):
    pass  # No constructor here

# Create object of child class
c = Child()

Output

Parent class constructor called

```

