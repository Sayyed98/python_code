class Student: 
    '''Developed by durga for python demo'''
    def __init__(self): 
        self.name='durga' 
        self.age=40
        self.marks=80 
    def talk(self): 
        print("Hello I am :",self.name) 
        print("My Age is:",self.age)
        print("My Marks are:",self.marks)

s1=Student()
s1.talk()