# Create a class ‘Employee’ and add salary and increment properties to it.


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # _salary is private
        self._increment = 0.10  # default increment is 10%
# __init__() is the constructor that runs when you create an object.

# self._salary and self._increment are private variables (indicated by underscore _) to discourage direct access.
#
# 🎯@property Decorator
# We use @property to make a method behave like an attribute (for better encapsulation).

    @property
    def salary(self):
        return self._salary
# This lets you access emp.salary instead of emp.get_salary()

    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Salary cannot be negative.")
        else:
            self._salary = value
# This lets you safely set the salary like emp.salary = 60000

# It checks that the salary is not negative.

# ✅ increment Property

    @property
    def increment(self):
        return self._increment
# Access emp.increment to get current increment rate

    @increment.setter
    def increment(self, value):
        if 0 <= value <= 1:
            self._increment = value
        else:
            print("Increment should be between 0 and 1")
# This validates the value (0 to 1 means 0% to 100%)

# ➕ Method: apply_increment()

    def apply_increment(self):
        self._salary = self._salary + (self._salary * self._increment)
# This applies the raise/increment to the salary.

# Example: If salary is 50,000 and increment is 10% (0.10), it becomes 55,000.

# 📋 Method: display()

    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: ₹{self._salary}")
        print(f"Increment Rate: {self._increment * 100}%")
# This just prints the current info in a readable format.


emp = Employee("John", 50000)  # Create object
emp.display()                  # Show initial values

emp.apply_increment()          # Increase salary by 10%
print("\nAfter applying increment:")
emp.display()                  # Show updated salary

emp.increment = 0.20           # Change increment to 20%
print("\nAfter setting new values:")
emp.salary = 60000             # Change salary
emp.display()                  # Final values


'''Class      ----	Blueprint to create objects (Employee)
__init__()    ----  Constructor for initialization
@property     ---- 	Getter to access a private variable
@x.setter     ----  Setter to validate and set new values
Encapsulation ----	Protect data using private variables
Object	      ----  Instance of a class'''

