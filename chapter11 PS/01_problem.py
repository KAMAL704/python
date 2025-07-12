'''Create a class (2-D vector) and use it to create another class representing a 3-D
vector'''
#  2D vector

class vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(f"2D vectors: ({self.x}, {self.y}")

    def magnitude(self):
        return (self.x**2 + self.y**2) ** 0.5
    
# 3D vectors(inherit from vector 2D)

class vector3D(vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)  #call vector 2D constructor
        self.z = z

    def display(self):
        print(f"3D vector: ({self.x}, {self.y}, {self.z})")

    def magnitude(self):
        return(self.x**2 + self.y**2 + self.z**2) **0.5
    

v2 = vector2D(3, 4)
v2.display()
print("magnitude of 2D vector:" , v2.magnitude())
print("            ")
v3 = vector3D(1, 2, 2)
v3.display()
print("magnitude of 3D vector:" , v3.magnitude())


'''🧠 Explanation
Vector2D handles x and y.

Vector3D inherits from Vector2D and adds z.

The super() function is used to call the parent class constructor.

Both classes have a display() and magnitude() method, but Vector3D overrides them.'''










class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j ")
        

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoDVector(1, 2)
a.show()
b = ThreeDVector(5, 2, 3)
b.show()