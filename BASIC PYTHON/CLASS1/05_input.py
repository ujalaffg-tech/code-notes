
#.type conversion 
#: digits ka type change karke str,int,floot kar sakte hain , 
a = str(5)
print(type(a)) 
b = float(2)
print(type(b))
c = int(4.08)
print(type(c))

x = "5"
d = int("5")
print(type(d))

x = "5"
y = "5"
print(x+y) ## ans = 55
# str ka type change nahi kar sakte
# a = float("aditya")
# print(type(a)) #= error

name = input( "enter  your name ")
age = (input( " enter your age "))
marks = (input(" enter your marks"))
print("welcome ", name)
print("age", age)           
#: input ka type by default str hota hain
