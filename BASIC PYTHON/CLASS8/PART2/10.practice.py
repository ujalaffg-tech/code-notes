'''Qs. Define a Circle class to create a circle with radius r 
using the constructor.
Define an Area method of the class which calculates the area of the circle.
Define a Perimeter method of the class which allows you to calculate
the perimeter of the circle.'''

class Circle :
    def __init__(self,radius):
        self.radius = radius

    def calc_area(self):
        print(3.14 * self.radius ** 2)
    
    def cal_perimeter(self):
        print(4 * 3.14 * self.radius)
    
c1 = Circle(6)
c1.calc_area()
c1.cal_perimeter()

''' Qs. Define a Employee class with attributes role, department & salary.
this class also a showDetails() method.
Create an Engineer class that inherits properties from Employee & has additional
attributes: name & age.'''
## second method se banaye hai

class Employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary
    
    def show_details(self):
        print("role =",self.role)
        print("departmenrt =",self.department)
        print("salary =",self.salary)

class Engineer(Employee):
    def __init__(self,role,department,salary,name,age):
        self.name = name 
        self.age = age
        super().__init__(role,department,salary)

    def latest_info(self):
        super().show_details()
        print("name =",self.name)
        print("age =",self.age)
    
e1 = Engineer("manager","it",40000,"nik",19)
print(e1.name)
e1.latest_info()


''' Qs. Create a class called Order which stores item & its price.
Use Dunder function ._gt._() to convey that:
order1 > order2 if price of order1 > price of order2 '''

class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,ord2): 
        print(self.price > ord2.price)

ord1 = Order("chips",5)
print(ord1)

ord2 = Order("campa",25)
ord2 > ord1
ord2 < ord1
ord1 < ord2
ord1 > ord2

