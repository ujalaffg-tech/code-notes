
#.staticmethods
#: iska use class & obj ke method me 
#: jab obj se matlab na ho tab use karenge

class Student:
    def __init__(self,name):
        self.name = name
    @staticmethod
    def hello():
        print("hello") ## iske liye obj metter hi nahi karta
s1 = Student("aditya")
s1.hello()
