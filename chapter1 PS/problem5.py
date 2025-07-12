''' q5 = Write a python program to print the contents of a directory using the os module.
 Search online for the function which does that
 ans = using chatgpt'''


import os

# Function to print directory contents
def print_directory_contents(path='/'):
    try:
        # Get the list of entries (files/folders) in the directory
        entries = os.listdir(path)
        
        print(f"Contents of {path}:")
        # Loop through the entries and print them
        for entry in entries:
            print(entry)

    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for directory '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with the current directory
print_directory_contents()

# To call it for a specific directory, provide the path like this:
# print_directory_contents("/path/to/your/directory")
