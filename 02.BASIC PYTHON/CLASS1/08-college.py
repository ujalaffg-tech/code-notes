
#. sep

print(10,20,30)
print(10,20,30, sep="-")

print("Ram", "Shyam", "Mohan",)
print("Ram", "Shyam", "Mohan", sep=",")

print("py","thon")
print("py","thon",sep="")

#. end

print("hello")
print("world")
print("adi",end = "")
print("08")
print("adi",end=" ")
print("in")
print("adi",end="\n")
print("08")
print("adi",end="\t")
print("08")
print("adi",end=".")
print("in")

print(1,2,3, end = "!",sep = "-")
print("Done")

#.  
a = [10, 20, 30]
b = a
print(a is b)

a = [10, 20, 30]
b = [10, 20, 30]
print(a is not b)

'''== aur is mein difference
| Code | Output | Reason |
|---|---|---|
| a = [1, 2], b = [1, 2] |
| a == b | True | Values same hain |
| a is b | False | Alag list objects hain |
| a is not b | True | Same object nahi hain |'''

a = [1,2]
b = [1,2]
print(a is b)
print(a is not b)
print(1 is a)

#. 
x = None
print(x is None)

# - BODMAS

''' Multiplication (*) aur Division (/) ki priority same hoti hai. 
Addition (+) aur Subtraction (-) ki priority bhi same hoti hai.
Jab priority same ho, toh left to right (baayein se daayein) 
solve karte hain.'''

print(10 - 3 + 2)
''' 10 - 3 = 7 — pehle left wala operation.
7 + 2 = 9 '''

#. in operator
fruits = ["apple", "mango", "banana"]
print("mango" in fruits)
print("grapes" in fruits)

#. not in operator
fruits = ["apple", "mango", "banana"]
print("mango" not in fruits)
print("grapes" not in fruits)


name = "Aditya"
print("A" in name)
print("z" in name)
print("dit" in name)
print("DIT" in name)

