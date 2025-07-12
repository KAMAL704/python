
'''a.items(): Returns a list of (key,value)tuples.
• a.keys(): Returns a list containing dictionary's keys.
• a.update({"friends":}): Updates the dictionary with supplied key-value pairs.
• a.get("name"): Returns the value of the specified keys (and value is returned
eg."harry" is returned here).'''

student = {"name": "John", "age": 21, "grade": "A"}

print(student.get("name"))        # John
print(student.get("gender", "N/A"))  # N/A (default returned)

print(student.keys())             # dict_keys(['name', 'age', 'grade'])
print(student.values())           # dict_values(['John', 21, 'A'])
print(student.items())            # dict_items([('name', 'John'), ('age', 21), ('grade', 'A')])

student.update({"age": 22})
print(student)                    # {'name': 'John', 'age': 22, 'grade': 'A'}

student.pop("grade")
print(student)                    # {'name': 'John', 'age': 22'}

student.clear()
print(student)                    # {}






marks = {
    "kamal": 98,
    "rahul": 67,
    "urmila": 43
}

print(marks.items())

print(marks.keys())

marks.update({"kamal": 89, "renuka": 100})
print(marks)

print(marks.get("kamal1"))  #none
print(marks["kamal1"])  # return error 