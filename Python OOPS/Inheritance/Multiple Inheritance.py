Multiple Inheritance

When a class inherits from more than one parent class, it's called multiple inheritance.

📌 Simple analogy:

A child gets qualities from both Mom and Dad.

```
class Father:
    def show_father(self):
        print("I am Father")

class Mother:
    def show_mother(self):
        print("I am Mother")

class Child(Father, Mother):
    def show_child(self):
        print("I am Child")

c = Child()
c.show_father()   # from Father
c.show_mother()   # from Mother
c.show_child()    # from Child

I am Father
I am Mother
I am Child



+-------------+     +-------------+
|   Father    |     |   Mother    |
+-------------+     +-------------+
        \             /
         \           /
         +-----------+
         |   Child   |
         +-----------+



class Developer:
    def code(self):
        print("Writes Python code")

class Designer:
    def design(self):
        print("Designs UI/UX")

class TechLead(Developer, Designer):
    def lead_team(self):
        print("Leads the Tech Team")


lead = TechLead()
lead.code()       # from Developer
lead.design()     # from Designer
lead.lead_team()  # from TechLead


Writes Python code
Designs UI/UX
Leads the Tech Team

```
Method Resolution Order (MRO):

Python uses the MRO (Left to Right) to decide which method to call if parents have the same method name.

The class listed first will be prioritized.

```
  class A:
    def greet(self): print("A")

class B:
    def greet(self): print("B")

class C(A, B): 
    pass

C().greet()  # Output: A

```
