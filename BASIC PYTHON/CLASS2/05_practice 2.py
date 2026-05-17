
#| WAP to find the greatest of 3 numbers entered by the user.
num1 = int(input("enter number 1 : "))
num2 = int(input("enter number 2 : "))
num3 = int(input("enter number 3 : "))
if(num1 >= num2 and num3):
    gn = num1
elif(num2 >= num3 and num1):
    gn = num2
else:
    gn = num3
print("greatest number is :",gn)

#- WAP to check if a number entered by the user is odd or even.
num = int(input("enter number : "))
if(num % 2 == 0):
    print("number is even")
else:
    print("number is odd")

#- WAP to check if a number is a multiple at 7 or not
num = int(input("enter number : "))
if (num%7 == 0):
    print(num,"is the multiples of 7")
else:
    print(num,"is the not multiples of 7")



