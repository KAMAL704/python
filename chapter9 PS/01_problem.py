'''Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word ‘twinkle’'''


f = open("poem.txt")
word = f.read()
if("twinkle" in word):
    print("The word is twinkle is present")

else:
    print("The word is twinkle is present")
f.close()