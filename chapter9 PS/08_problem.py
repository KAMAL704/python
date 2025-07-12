# Write a program to make a copy of a text file “this. txt”


with open("This.txt", "r") as f:
    content = f.read()


with open("This_copy.txt", "w") as f:
    f.write(content)