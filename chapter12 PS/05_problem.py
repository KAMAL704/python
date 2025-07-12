# Store the multiplication tables generated in problem 3 in a file named Tables.txt.


n = int(input("Enter a num"))

table = [n*i for i in range(1, 11)]
print(table)

with open("Table,txt", "a") as f:  
    f.write(f"table of {n}: {str(table)} \n")