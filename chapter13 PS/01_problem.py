'''Write a program to input name, marks and phone number of a student and format it
using the format function like below:'''

name = input("Enter name")
marks = int(input("Enter marks"))
phone = int(input("Enter phone no"))

s = "The name is {}, and marks {}, and phone no {}".format(name, marks, phone)
print(s)