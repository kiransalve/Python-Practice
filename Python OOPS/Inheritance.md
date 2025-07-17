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


Scenario 3

If both the parent and child class have their own constructor (__init__), then only the child's constructor is called when creating an object of the child class.

```text

class Parent:
    def __init__(self):
        print("Parent Constructor")

class Child(Parent):
    def __init__(self):
        print("Child Constructor")

# Create object of Child class
c = Child()

Output:

Child Constructor

```

Scenario 4

parameter vs instance variable” situation

```text

class A:
    def __init__(self):
        self.var1 = 100

    def display1(self, var1):
        print("Class A : ", self.var1)

class B(A):
    def display2(self, var1):
        print("Class B : ", self.var1)

obj1 = B()
obj1.display1(200)

Output:

Class A :  100
```

Why 100 (not 200)?

obj1 = B() → B has no __init__, so Python automatically calls A’s __init__, setting self.var1 = 100.

When you call obj1.display1(200), the method receives var1=200 as a parameter, but it never uses it

Scenario 5

call parent class methods or constructor from a child class

super() is used to call parent class methods or constructor from a child class — especially useful in inheritance.

1 Calling Parent Constructor in Child Class

```text


class A:
    def __init__(self):
        print("Constructor of A")

class B(A):
    def __init__(self):
        super().__init__()  # calls A's constructor
        print("Constructor of B")

obj = B()

Output

Constructor of A  

Constructor of B

```
2 Calling Parent Method
 
```text

class A:
    def show(self):
        print("A's show")

class B(A):
    def show(self):
        super().show()  # calls A's show
        print("B's show")

obj = B()
obj.show()

Output

A's show  

B's show

```

3 In Multiple Inheritance (MRO)

```text
class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

class C(B):
    def __init__(self):
        super().__init__()
        print("C")

obj = C()

Output

A  

B  

C

```

When to Use super()?

When extending functionality of the parent method.

When you want to reuse parent constructor logic.

In multiple inheritance, it follows MRO (Method Resolution Order) to ensure correct method calls

