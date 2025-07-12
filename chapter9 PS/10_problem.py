# Write a program to wipe out the content of a file using python.

with open("This_copy.txt", "w") as f:
    f.write("")    

# another method


with open("This_copy.txt", "w") as f:
    pass