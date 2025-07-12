'''Create a class with a class attribute a; create an object from it and set ‘a’
directly using ‘object.a = 0’. Does this change the class attribute?'''

class MyClass:
    a = 10  # class attribute

obj = MyClass()     # create an object
obj.a = 0           # set 'a' using object

print("obj.a =", obj.a)          # 0 (instance attribute)
print("MyClass.a =", MyClass.a)  # 10 (class attribute)
