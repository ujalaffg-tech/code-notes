class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math )/3) + "%"

    def percentage_(self):
        print("percentage = ",self.percentage) 

s1 = Student(50,60,70)
s1.percentage_()
s1.math = 100
print(s1.math)
s1.percentage_() ## percentage ka val cahnge hona chahiye tha lakin nahi hua 

#. property method
#: yah attr ka latest change dikhata hain

class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math )/3) + "%"

    @property
    def calc_percentage(self):
        print("percentage = ",self.percentage)

s1 = Student(50,30,10)
s1.calc_percentage
s1.math = 100
s1.calc_percentage