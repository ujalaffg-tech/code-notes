
#| write a python program to take three different numbers
#| and print the number that lies between the other two numbers.

a = int(input("enter number : "))
b = int(input("enter number : "))
c = int(input("enter number : "))
if (a<b and a>c)  or (a<c and a>b):
    print(a)
elif (b<a and b>c) or (b<c and b>a) :
    print(b)    
elif (c<a and c>b) or (c>a and c<b):
    print(c)



    

