
#.multi-level enheritance

class Car:                          ## parent class

    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class Toyota(Car):                  ## child class
    def __init__(self,brand):
        self.brand = brand

class Fortuner(Toyota):             ## child class
    def __init__(self,type):
        self.type = type

c1 = Fortuner("diesel")
c1.start()

#.multiple enheritance
class A:
    var1 = "welcome to class A"

class B:
    var2 = "welcome to class B"

class C:
    var3 = "welcome to class C"

class D(A,B,C):
    var4 = "welcome to class D"

d1 = D()
print(d1.var3)
