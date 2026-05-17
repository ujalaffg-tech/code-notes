

## str
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"student = {self.name} , marks = {self.marks}"

s1 = Student("aditya",90)
print(s1)

## len
class Book:
    def __init__(self,title,price):
        self.title = title 
        self.price = price

    def __len__(self):
        return len(self.title)
b1 = Book("python",500)
print(len(b1))

