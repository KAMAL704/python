class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45

e.show()




'''Use a class method when:

-You want to access or modify class variables.

-You want to create alternative constructors (like from_string()).

-The logic of the method is related to the class, not to the instance.'''

class MyClass:
    class_variable = 0

    @classmethod
    def my_class_method(cls, value):
        cls.class_variable = value

print(MyClass.class_variable)
MyClass.my_class_method("class 1")
print(MyClass.class_variable)
