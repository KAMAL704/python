'''Write a class “Calculator” capable of finding square, cube and square root of a
number'''


class Calculator:
    def __init__(self, n):
        self.n =  n

    def square(self):
        print(f"The square is {self.n*self.n}")    


    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")    


    def squareroot(self):
        print(f"The squareroot is {self.n**0.5}")    

a = Calculator(8)
a.square()
a.cube()
a.squareroot()

