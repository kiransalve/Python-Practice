Aggregation is a special type of Object-Oriented Programming (OOP) relationship where:

One class has-an object of another class, but both can exist independently

"A car has an engine" — the engine exists separately but is used by the car.

```text
class Address:
    def __init__(self, city, pincode):
        self.city = city
        self.pincode = pincode

class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address  # Aggregation (uses Address object)
    
    def show(self):
        print(f"{self.name} lives in {self.address.city} - {self.address.pincode}")

addr1 = Address("Mumbai", "400001")
emp1 = Employee("Kiran", addr1)

emp1.show()  # 👉 Kiran lives in Mumbai - 400001

# Address object still exists even without Employee
print(addr1.city)  # 👉 Mumbai

```
Employee has-a Address

Even if you delete emp1, addr1 still exists

This is aggregation — loose connection between objects

