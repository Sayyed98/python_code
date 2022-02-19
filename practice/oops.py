from unicodedata import name


class car():
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(age)
    def address(self):
        self.name=name
obj=car()
obj.name("mohd hhujaifa")
obj.age(22)