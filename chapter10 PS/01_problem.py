'''Create a class “Programmer” for storing information of few programmers
working at Microsoft.'''

class programmer:
    company = "microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("kamal", 120000, 335523)
print(p.name, p.salary, p.pin, p.company)