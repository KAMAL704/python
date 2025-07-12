'''Write a program to print third, fifth and seventh element from a list using enumerate
function.'''

l = [1, 2, 3, 4, 5, 6, 7, 8]

for i, item in enumerate(l):
    if i ==2 or i == 4 or i ==6:
        print(item)







# Sample list
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Using enumerate to access elements with their indices
for index, value in enumerate(my_list):
    if index in [2, 4, 6]:  # 3rd, 5th, and 7th elements (0-based index)
        print(f"Element at position {index + 1} is: {value}")

