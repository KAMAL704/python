# Doveloped by Guido Van Rossume in 1993.


"""2. Memory Allocation Types

Python internally दो तरह से memory allocate करता है:

Stack Memory:

Local variables और function calls store करता है।

Temporary होता है (function खत्म होते ही clear हो जाता है)।

Heap Memory:

Objects (list, dict, class instances) store करता है।

Automatically managed by Garbage Collector।"""

x = 5
id(x)
print(id(x))