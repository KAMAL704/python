'''Write a Class ‘Complex’ to represent Complex numbers, along with overloaded
operators ‘+’ and ‘*’ whiCh adds and multiplies them.'''


class Complex:

    def __init__(self, real, img):
        self.real = real  #real part
        self.img = img    #img part

    def __add__(self, other):
        # overload + operator
        return Complex(self.real + other.real, self.img + other.img)
        

    def __mul__(self, other):
        # overload * operator
        real = self.real * other.real - self.img * other.img
        img = self.img * other.real + self.real * other.img
        return Complex(real, img)

    def __str__(self):
        # For printing in the form a + bi
        return f"{self.real} + {self.img}i"
        

C1 = Complex(3, 6)
C2 = Complex(4, 5)

print("First Complex num is:", C1)
print("SeCondComplex num is:", C2)

C3 = C1 + C2
print("Addition:", C3)

C4 = C1*C2
print("MultipliCation:", C4)