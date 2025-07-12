class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def __init__(self, name, language, salary):  #dunder method which is autometic call.
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    


    @staticmethod
    def greet():
        print("Good morning")


harry = Employee("harry", 12000, "java")
# harry.language = "JavaScript" # This is an instance attribute
# harry.greet()
# Employee.greet(harry)
# harry.getInfo() 
# Employee.getInfo(harry)
print(harry.name, harry.salary, harry.language)
