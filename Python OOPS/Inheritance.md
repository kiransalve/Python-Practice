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
   

Scenario - 1

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


Scenario - 2

If both the parent and child class have a method with the same name, then the child's method overrides the parent's method. This is called Method Overriding in OOP.

```text

class Parent:
    def show(self):
        print("This is Parent method")

class Child(Parent):
    def show(self):
        print("This is Child method")

# Create object of child class
c = Child()
c.show()

Output

This is Child method
```

Even though Child inherits from Parent, when you call c.show(), it will use the Child's version of show() method.

This is polymorphism: same method name, different behavior.

suppose my father has family business, but I choose softwere developer as career

my father choose there career as business but I have freedom to choose father's business but I will choose mine


