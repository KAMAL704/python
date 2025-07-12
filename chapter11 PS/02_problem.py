'''Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from
‘Pets’. Add a method ‘bark’ to class ‘Dog’.'''


class Animals:
    pass 

class Pets(Animals):
    pass 

class Dog(Pets):

    @staticmethod
    def bark():
        print("Bow Bow!")


d = Dog()

d.bark()


#############

# Base class
class Animals:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived class from Animals
class Pets(Animals):
    def __init__(self, name):
        super().__init__(name)

# Derived class from Pets
class Dog(Pets):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

# Testing the classes
d = Dog("Buddy")
d.speak()   # Inherited from Animals
d.bark()    # Dog-specific method