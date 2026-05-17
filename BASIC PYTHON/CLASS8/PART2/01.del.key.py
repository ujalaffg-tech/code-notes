
#: iska use class ko delete ya class ke attr ko del ke liye karte hain
class Student:
    def __init__(self,name):
        self.name = name
    
s1 = Student("aditya")
print(s1)
del s1
print(s1.name)