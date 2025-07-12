# \n  = new line
# \t = tab
# \; = singlequote
# \\ =  backslash


# 2. Tab (\t)
# Inserts a horizontal tab.

# print("Name\tAge")
# print("John\t25")
# Output:

# Name    Age
# John    25

# 3. Backslash (\\)
# Inserts a backslash.

# print("This is a backslash: \\")
# Output:

# This is a backslash: \


# 4. Single Quote (\')
# Inserts a single quote in a string enclosed by single quotes.

# print('It\'s a sunny day')
# Output:
#
# It's a sunny day


# 5. Double Quote (\")
# Inserts a double quote in a string enclosed by double quotes.

# print("He said, \"Hello!\"")
# Output:

# He said, "Hello!"


# 6. Carriage Return (\r)
# Moves the cursor to the beginning of the line.

# print("12345\rabc")
# Output:

# abc45

# 7. Bell (\a)
# Makes a beep sound (depends on system).

# print("\a")
# (May produce a beep sound if your system supports it)
# 
# 🔹 Raw String (ignoring escape sequences)
# Use r"" to prevent escape sequences from being interpreted:

# print(r"C:\new_folder\test.txt")
# Output:

# C:\new_folder\test.txt



a = "rahul  is a good boy \n but not a bad boy"
print(a)    #\n   - new line


a = "rahul  is a good boy \\ but not a bad \"boy\""
print(a)
# 