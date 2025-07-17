self is object, becouse all things in python is object.

agar vo object hai to uska koi id hoga, memory address hoga

jis bhi object ke sath app abhi kam kar rahe ho vahi self hai

Why in every method self should be give as argument?

```text

class Person:
    def __init__(self, name):
        self.name = name  # store name in this object

    def say_hello(self):
        print(f"Hello, my name is {self.name}")
```

```text

p1 = Person("Kiran")
p1.say_hello()  # 👉 Hello, my name is Kiran

```

When you call p1.say_hello(), Python automatically does this:

```text
Person.say_hello(p1)  # `self` becomes `p1`
```
self.name becomes p1.name

That’s how the method accesses the data stored inside p1

Class ke pe pas kya hota hai, ek to data hota hai, dusre methods hote hai

aur wo data kiska hota hai, wo hota hai objects ka

agar sbi aur hdfc do object hai, un dono ka data alag hoga

sbi, hdfc ka data access nahi kar sakta, kyonki sbi object ka data access karne ka authority sirf sbi ke pass hai dusre ke pass nahi

self is basically current object
