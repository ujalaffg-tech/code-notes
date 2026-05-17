
## constructer ke liye
class Animal:
    def __init__(self,name):
        self.name = name

class Dog(Animal):
    def __init__(self,name,brid):
        super().__init__(name)
        self.brid = brid

class Puppy(Dog):
    def __init__(self,name,brid,color):
        super().__init__(name,brid)
        self.color = color

z1 = Puppy("Zimmy","labrador","kala")
print(z1.name)

## method ke liye 
class Person:
    def __init__(self,name,base_price):
        self.name = name
        self.base_price = base_price

    def get_price(self):
        print("product =",self.name)
        print("base_price =",self.base_price)

class Taxeble_prod(Person):
    def __init__(self,name,base_price,tax_percent):
        super().__init__(name,base_price) ##
        self.tax_percent = tax_percent

    def get_price_with_tax(self):
        super().get_price() ##
        print("hello")

t1 = Taxeble_prod("abc",100,"28%")
t1.get_price_with_tax()