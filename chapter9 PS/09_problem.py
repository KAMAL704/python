'''Write a program to find out whether a file is identical & matches the content of
another file'''

with open("This.txt", "r") as f:
    content1 = f.read()


with open("This_copy.txt", "r") as f:
    content2 = f.read()


if(content1 == content2):
    print("yes these file is identical")

else:
    print("No these file is not identical")