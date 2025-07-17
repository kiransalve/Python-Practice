It means restricting direct access of data (variables) and methods (functions) to some of the object's components data

example 
```text
class ATM:
  def __init__(self):
      self.__balance = balance

```
when we add "__" (double under score) to variable or method name, it is not accessible to object

internally python store it as

__balance ----> _ATM__balance

so if anyone accidently access like sbi._balance, it does not affect the original balance data, becasue it store different name (_ATM__balance).

but if anyone access it by _ATM__balance, then it will changed.

so Nothing in python is truely private

why, because python is language made for Adults.

when you use double under score it is gentlemens agreements that this is my private variable, don't use it, and other should not use it

and if other want to crash your softwere by using it, it is enmity of two human, it is not language fault.

also python not completely hide because in future if you need to ulter the variable, then you can.

We make two functions - get() and set() to get and ulter the private variable but with our own custom logic.

