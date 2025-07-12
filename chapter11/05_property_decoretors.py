# without attribute

class Student:
    def __init__(self, marks):
        self._marks = marks

    def get_marks(self):
        return self._marks

s = Student(90)
print(s.get_marks())  # Access like a method


# with attribute
class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

s = Student(90)
print(s.marks)  # Access like an attribute

# setter

class Student:
    def __init__(self):
        self._marks = 0

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            print("Invalid marks. Must be between 0 and 100.")

s = Student()
s.marks = 85       # Uses setter
print(s.marks)     # Uses getter
s.marks = 150      # Invalid marks

# deleter
class Student:
    def __init__(self):
        self._marks = 75

    @property
    def marks(self):
        return self._marks

    @marks.deleter
    def marks(self):
        print("Deleting marks...")
        del self._marks

s = Student()
print(s.marks)  # 75
del s.marks     # Deletes the _marks attribute
