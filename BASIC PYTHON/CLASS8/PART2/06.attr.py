class Person:
    name = "anonymous"

    def __init__(self,name):
        self.name = name

p1 = Person("RAHUL")
print(p1.name)
print(Person.name)

## class method
class Person:
    name = "anonymous"

    @classmethod
    def change_name(cls,name):
        cls.name = name 
        

p1 = Person()
p1.change_name("adi")
print(p1.name)
print(Person.name)

## instance method
class Person:
    name = "anonymous"

    def change_name(self,name):
        self.__class__.name = name

p1 = Person()
p1.change_name("nik")
print(p1.name)
print(Person.name)