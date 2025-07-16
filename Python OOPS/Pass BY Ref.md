"pass by reference" means passing the memory address of a variable into a function, not just a copy of its value. So if the function modifies the parameter, the original variable is also modified.

Imagine you gave your friend the original house key (reference). They can now go inside and change your furniture (the actual variable).

In contrast, if you gave a photo (copy), they can look at it but can’t change the real furniture.

Python doesn’t strictly use "pass by reference" or "pass by value". Instead, it passes "object references".

Mutable	Like list, dict, set → changes inside function affect original

Immutable	Like int, float, str, tuple → changes do not affect original

