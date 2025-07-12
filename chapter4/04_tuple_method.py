
'''1. count()
Returns the number of times a specified value appears in the tuple.


tuple.count(value)
Example:
t = (1, 2, 2, 3, 2, 4)
print(t.count(2))  # Output: 3

2. index()
Returns the index of the first occurrence of a specified value.

tuple.index(value)
You can also specify the optional start and stop parameters:

tuple.index(value, start, stop)
Example:

t = (10, 20, 30, 20)
print(t.index(20))         # Output: 1
print(t.index(20, 2))      # Output: 3'''









a = (1, 34, 56, 343, "kamal", "vikash", False, 56)
print(a)  


no = a.count(56)
print(no)

no = a.index(343)
print(no)