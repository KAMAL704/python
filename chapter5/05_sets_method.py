'''a = {1, 2, 3}
b = {3, 4, 5}

a.add(4)                  # a = {1, 2, 3, 4}
a.update([5, 6])          # a = {1, 2, 3, 4, 5, 6}
a.remove(2)               # a = {1, 3, 4, 5, 6}
a.discard(10)             # No error, nothing happens
val = a.pop()             # Removes a random element
a.clear()                 # a = set()

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))         # {1, 2, 3, 4, 5}
print(a.intersection(b))  # {3}
print(a.difference(b))    # {1, 2}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}'''


s = {2, 4, 65, 4, 6, 5, 6, "kumar"}
s.add(76)

print(s, type)
s.remove(2)
print(s, type)
