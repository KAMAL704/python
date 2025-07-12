'''What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?'''



s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(len(s))  #output = 2  because in python 20 == 20.0


''' Expression               | Result  | Reason                                 |
    | ---------------------- | ------- | -------------------------------------- |
    | 1 == 1.0               | True    | Values are equal after type promotion. |
    | type(1) == type(1.0)   | False   | int ≠ float '''                      


