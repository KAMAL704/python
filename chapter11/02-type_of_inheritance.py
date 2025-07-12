
''' | Type         | Description                    |
    | ------------ | ------------------------------ |
    | Single       | One parent → one child         |
    | Multiple     | Many parents → one child       |
    | Multilevel   | Grandparent → Parent → Child   |
    | Hierarchical | One parent → multiple children |
    | Hybrid       | Combination of the above       |'''



# class Parent:
    # Parent class definition

# class Child(Parent):
    # Child class definition (inherits from Parent)



# single inheritance
class Animal:
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def bark(self):
        print("Woof!")

dog = Dog()
dog.sound()  # Inherited
dog.bark()   # Own method


# multilevel inheritance
class Grandfather:
    def property(self):
        print("House and Land")

class Father(Grandfather):
    def car(self):
        print("Car")

class Son(Father):
    def bike(self):
        print("Bike")

s = Son()
s.property()
s.car()
s.bike()

# Hierarchical Inheritance
# Multiple child classes inherit from the same parent class.
class Shape:
    def area(self):
        print("Calculating area...")

class Circle(Shape):
    def radius(self):
        print("Radius of circle")

class Rectangle(Shape):
    def length(self):
        print("Length of rectangle")

c = Circle()
r = Rectangle()
c.area()
r.area()


# Multiple Inheritance
# A child class inherits from more than one parent class.


class mother:
    def cooking(self):
        print("mother cooked food")

class father:
    def driver(self):
        print("father drive car")


class child(mother, father):
    def studying(self):
        print("child studies")

c = child()
c.cooking()
c.driver()
c.studying()