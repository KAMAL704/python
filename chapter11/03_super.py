class parents:
    def show(self):
        print("parent method")

class child(parents):
    def show(self):
        super().show()   # calls Parent's show()
    print("child method")


c = child()
c.show()