```text

# 🧠 Types of Inheritance in Python

---

## 1. 🟦 Single Inheritance  

> One child class inherits from one parent class.


  ┌─────────┐
  │ Parent  │
  └────┬────┘
       │
       ▼
  ┌─────────┐
  │  Child  │
  └─────────┘


```python
class Parent:
    pass

class Child(Parent):
    pass


2. 🟩 Multiple Inheritance

One child inherits from more than one parent.


  ┌─────────┐   ┌─────────┐
  │ Parent1 │   │ Parent2 │
  └────┬────┘   └────┬────┘
       └──────┬──────┘
              ▼
         ┌─────────┐
         │  Child  │
         └─────────┘

class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass

3. 🟨 Multilevel Inheritance

Inheritance through multiple generations.


    ┌────────────┐
    │ Grandparent│
    └────┬───────┘
         ▼
     ┌─────────┐
     │ Parent  │
     └────┬────┘
          ▼
     ┌─────────┐
     │  Child  │
     └─────────┘

class Grandparent:
    pass

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

4. 🟧 Hierarchical Inheritance

Multiple children inherit from the same parent.


           ┌─────────┐
           │ Parent  │
           └────┬────┘
        ┌───────┴────────┐
        ▼                ▼
   ┌─────────┐      ┌─────────┐
   │ Child1  │      │ Child2  │
   └─────────┘      └─────────┘


class Parent:
    pass

class Child1(Parent):
    pass

class Child2(Parent):
    pass

5. 🟥 Hybrid Inheritance

Combination of multiple types of inheritance.

  ┌─────────┐   ┌─────────┐
  │ Parent1 │   │ Parent2 │
  └────┬────┘   └────┬────┘
       ▼            ▼
     ┌─────────────────┐
     │  Intermediate   │
     └──────┬──────────┘
            ▼
       ┌─────────┐
       │  Child  │
       └─────────┘

class Parent1:
    pass

class Parent2:
    pass

class Intermediate(Parent1, Parent2):
    pass

class Child(Intermediate):
    pass
```
