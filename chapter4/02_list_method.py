'''l1 = [1,8,7,2,21,15]
• l1.sort(): updates the list to [1,2,7,8,15,21]
• l1.reverse(): updates the list to [15,21,2,7,8,1]
• l1.append(8): adds 8 at the end of the list
• l1.insert(3,8): This will add 8 at 3 index
• l1.pop(2): Will delete element at index 2 and return its value.
• l1.remove(21): Will remove 21 from the list. '''

friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends)
friends.append("kamal")
print(friends)


friends = [1, 2, 4, 8, 54, 45]
friends.sort()
print(friends)

friends = [1, 2, 4, 8, 54, 45]
friends.reverse()
print(friends)

friends = [1, 2, 4, 8, 54, 45]
friends.insert(2, 7)
print(friends)

friends = [1, 2, 4, 8, 54, 45]
friends.pop(2)
print(friends)

friends = [1, 2, 4, 8, 54, 45]
friends.remove(45)
print(friends)

