Use Cases 1

```text

class Phone:
    def __init__(self, price, brand, camera):
        print("Step 2 - Inside Phone contructor")
        self.price=price
        self.brand=brand 
        self.camera=camera

class Smartphone(Phone):
    def __init__(self,price, brand, camera, os, ram):
        print("Step 1 - Smartphone contructor")
        super().__init__(price,brand,camera)
        self.os = os
        self.ram = ram
        print("Step 3 - Inside Smartphone contructor with updated os and ram")

s = Smartphone(2000, "Samsumg", 12, "Android",2)
print(s.os,s.ram,s.camera,s.price)

```

first s is object created with price, brand, camera, os and ram

child class has its own contructor, so it will run first

using super() we called parents contructor and send price, brand and camera, becasue these are common features of phones

then parents contructor saved these

then child class save os and ram which is smartphone specific 


Use Case 2

```text

class Parent:
    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num
    
class Child(Parent):
    def __init__(self, num, val):
        super().__init__(num)
        self.__val=val
    
    def get_val(self):
        return self.__val
    
son = Child(100, 200)

print(son.get_val())
print(son.get_num())

```

Use Case 3

```text

class Parent:
    def __init__(self):
        self.num = 100

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.var = 200
    def show(self):
        print(self.num)
        print(self.var)

son= Child()
son.show()

```

When a Parent object is created, it sets num = 100.

Child is inheriting from Parent.

Inside Child's constructor (__init__), super().__init__() is used to call the Parent constructor.

So, self.num = 100 is executed from the parent.

Then self.var = 200 is set.

show() function prints both values: num from parent and var from child.

A new object son of class Child is created:

It runs the Child constructor.

super().__init__() runs Parent constructor → sets self.num = 100.

Then self.var = 200 is set.

Then son.show() prints:

100
200

Here is key concept that inside child we can get parents attributes

outside of class we call it like - son.var and inside of class we call it like - self.var

because son and self are same here

jaise gangadhar hi shaktiman hai vaise - son hi self hai
