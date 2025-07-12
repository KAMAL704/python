''' q5 = Write a python program to print the contents of a directory using the os module.
 Search online for the function which does that
 ans = using chatgpt'''





import os


#  specify the directory you want to list
direcotory_path = '/'

contents = os.listdir(direcotory_path)
for item in contents:
    print(item)