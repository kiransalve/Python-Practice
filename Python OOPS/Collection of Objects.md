A collection of objects refers to a group (or container) that stores multiple instances of a class (i.e., objects). It's commonly used to manage and operate on a set of similar items.

Let’s say you have a Student class and want to store many students in one place — like a list or dictionary.

```text
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(f"{self.name}: {self.marks}")


 Create a Collection (like list) of Objects

 students = [
    Student("Alice", 85),
    Student("Bob", 90),
    Student("Charlie", 78)
]


 Loop Through Collection

 for s in students:
    s.show()



Output

Alice: 85

Bob: 90

Charlie: 78

```

| Type    | Description                         | Example                  |
| ------- | ----------------------------------- | ------------------------ |
| `list`  | Ordered, indexed, allows duplicates | `[obj1, obj2, obj3]`     |
| `set`   | Unordered, no duplicates            | `{obj1, obj2}`           |
| `dict`  | Key-value mapping                   | `{101: obj1, 102: obj2}` |
| `tuple` | Immutable ordered collection        | `(obj1, obj2)`           |

