class Employee: 
    language = "Py" # This is a class attribute
    salary = 1200000


harry = Employee()
harry.name = "Harry" # This is an object/instance attribute
harry.language = "java"
print(harry.name, harry.language, harry.salary)
