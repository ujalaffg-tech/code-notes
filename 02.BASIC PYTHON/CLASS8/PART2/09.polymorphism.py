
#.Polymorphism: Operator Overloading
#: When the same operator is allowed to have different meaning
#: according to the context.
## ex 
print (1 + 2) #-3
print ("apna" + "college") #- concatenate print
([1, 2, 3] + [4, 5, 6]) #- merge

class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    
    def show_num(self):
        print(self.real,"i +",self.imag,"j")

c1 = Complex(4,5)
c1.show_num()
c2 = Complex(8,6)
c2.show_num()

class Student:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def dekho_number(self):
        print(self.real,"i +",self.imag,"j")

    def __add__(obj1,obj2): ## Dunder Function
        new_real = obj1.real + obj2.real
        new_imag = obj1.imag + obj2.imag
        return Student(new_real,new_imag)


num1 = Student(4,5)
num1.dekho_number()

num2 = Student(8,7)
num2.dekho_number()

num3 = num1 + num2
num3.dekho_number()

