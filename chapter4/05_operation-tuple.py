# 1. Concatenation
# Join two tuples using the + operator.

t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)  # Output: (1, 2, 3, 4)

# 2. Repetition
# Repeat a tuple using the * operator.

t = (1, 2)
print(t * 3)  # Output: (1, 2, 1, 2, 1, 2)


# 3. Membership Testing
# Check if an item exists using in or not in.

t = (1, 2, 3)
print(2 in t)       # Output: True
print(4 not in t)   # Output: True

#
# 4. Indexing
# Access individual elements using square brackets.

t = (10, 20, 30)
print(t[1])  # Output: 20


# 5. Slicing
# Access a range of elements using slice notation.

t = (0, 1, 2, 3, 4)
print(t[1:4])  # Output: (1, 2, 3)


# 6. Length
# Use len() to find how many items are in the tuple.

t = (1, 2, 3)
print(len(t))  # Output: 3


# 7. Unpacking
# Assign each element to a variable.

t = (1, 2, 3)
a, b, c = t
print(a, b, c)  # Output: 1 2 3


# 8. Nested Tuples
# Tuples can contain other tuples.

t = (1, (2, 3), 4)
print(t[1][0])  # Output: 2


# 9. Conversion Between Tuple and List
# To "modify" a tuple, convert it to a list, change it, then convert back.

t = (1, 2, 3)
lst = list(t)
lst.append(4)
t = tuple(lst)
print(t)  # Output: (1, 2, 3, 4)
