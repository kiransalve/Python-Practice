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

