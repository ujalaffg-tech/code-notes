class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def kuch_bhi(self):
        print("......hat thari..")
    def hello(self):
        print("hello",self.name)
    def x(self):
        return self.marks
s1 = Student("jakir",69)
print(s1.x())
s1.hello()
s1.kuch_bhi()