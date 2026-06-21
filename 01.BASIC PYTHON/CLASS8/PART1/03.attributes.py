class Student:
    college_name = "bps college" ## class attributes
    def __init__(self,name,classes):
        self.name = name ## obj attributes
        self.classes = classes 
        
s1 = Student("aditya",12)
print(s1.name)
print(Student.college_name) 
print(s1.college_name) 

class Students:
    name = "anonymous" #: jo chije common ho sare obj ke liye
    #: to ushe class attribute bana dete hain 
    def __init__(self,name):
        self.name = name ## obj attr > class attr
s2 = Students("karan")
print(s2.name)   