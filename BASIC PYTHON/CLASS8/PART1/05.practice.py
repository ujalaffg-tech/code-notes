'''Create student class that takes name & 
marks of 3 subjects as arguments in constructor.
Then create a method to print the average.'''
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def avg(self):
        idx = 0
        for val in self.marks:
            idx += val
        print(idx/3)
s1 = Student("aditya",[30,60,99])
s1.avg()