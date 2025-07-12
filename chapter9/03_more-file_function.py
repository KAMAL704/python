# f = open("file.txt")
# l1 = f.readline()
# print(l1, type(l1))
# l2 = f.readline()
# print(l2, type(l2))
# f.close()

f = open("file.txt")
l = f.readline()
while(l != ""):
    print(l)
    l = f.readline()
    f.close