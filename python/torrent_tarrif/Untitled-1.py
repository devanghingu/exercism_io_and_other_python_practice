class abc:
    def __init__(self):
        pass
    def getname(self):
        self.name=input("enter name")
    def display(self):
        print(self.name)

a=abc()
a.getname()
a.display()