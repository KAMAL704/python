'''What is Operator Overloading in Python?
Operator Overloading allows us to define or change the behavior of operators (+, -, *, ==, etc.) for user-defined classes.'''

# In Python, everything is an object — so even operators like + can be customized using special methods (also called magic methods or dunder methods).

# 🔧 Why Use Operator Overloading?
'''To make class instances behave like built-in types.

To perform custom operations using operators.

Makes code more readable and intuitive.'''

# ✅ Example Without Operator Overloading

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(1, 2)
p2 = Point(3, 4)

# This will raise an error:
print(p1 + p2)  # ❌ TypeError

# ✅ Now With Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overloading '+'
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):  # String representation
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3)  # Output: (4, 6)
''' ⚙️ Common Magic Methods for Operator Overloading
Operator	Method	Example
+	__add__()	a + b
-	__sub__()	a - b
*	__mul__()	a * b
/	__truediv__()	a / b
//	__floordiv__()	a // b
%	__mod__()	a % b
**	__pow__()	a ** b
==	__eq__()	a == b
!=	__ne__()	a != b
<	__lt__()	a < b
<=	__le__()	a <= b
>	__gt__()	a > b
>=	__ge__()	a >= b'''

# 🧪 Example: Overloading ==

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __eq__(self, other):  # Overload ==
        return self.pages == other.pages

b1 = Book(100)
b2 = Book(100)
print(b1 == b2)  # True

# 🧮 Example: Overloading * for custom multiplication
class Vector:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):  # Multiply
        return Vector(self.value * other.value)

    def __str__(self):
        return str(self.value)

v1 = Vector(5)
v2 = Vector(3)
v3 = v1 * v2
print(v3)  # Output: 15
'''📝 Summary
Term	Meaning
Operator Overloading	Customizing operators for user-defined class objects
Magic Methods	Special methods like __add__, __eq__, __str__, etc
Benefit	Cleaner, readable code; behaves like built-in types'''