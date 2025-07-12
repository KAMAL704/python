'''Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}'''



''' | Element Type          | Can be in Set? | Why                    |
    | --------------------- | -------------- | ---------------------- |
    | int, str, tuple       | ✅ Yes        | Immutable and hashable |
    | list, dict, `set      | ❌ No         | Mutable and unhashable |'''
