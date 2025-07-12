# Write a program to filter a list of numbers which are divisible by 5.


def divisibles5(n):
    if(n%5 ==0):
        return True
    return False

l = [1,5,10,22,50,25]

f = list(filter(divisibles5, l))
print(f)


