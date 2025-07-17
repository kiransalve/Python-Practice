A static method is a method inside a class that:

Does NOT take self or cls as the first argument

Does NOT depend on instance (self) or class (cls) variables

Is used when you want to logically group a function inside a class, but don’t need access to class or object data

```text

class ATM:
    # ✅ Static variable (shared by all objects)
    account_count = 0

    def __init__(self, name):
        self.name = name
        ATM.account_count += 1  # increase count when new account created

    @staticmethod
    def get_total_accounts():
        return ATM.account_count

a1 = ATM("Kiran")
a2 = ATM("Rahul")
a3 = ATM("Sneha")

print(ATM.get_total_accounts())  # 👉 3
```

