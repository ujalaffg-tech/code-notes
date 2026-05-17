
#.arithmetic operators
a = 5
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)  ## remainder 
print(a ** b)  #(5 ** 2) = 25
               #(5 ** 3) = 125

#.relational operators
a = 50
b = 20
print(a == b) ##False
print(a != b) #True
print(a >= b) #True
print(a > b) #True
print(a <= b) #False
print(a < b) #False


#.assignment operators.                                                            
num = 10
num = num + 10 
print(num)
#isko ab aise likhenge 
num += 10
print(num)
num -= 20 #print(num) = -10
num *= 20
num /= 5
num **= 2
num %= 7

#.logical operators 
#| or operator
x = 5
y = 7 
case1 = x<=y
case2 = y>=x
print(case1 or case2)
case1 = x>=y
case2 = y>=x
print(case1 or case2)
case1 = x>=y
case2 = y<=x
print(case1 or case2)
#| and operator
a = 50
b = 78
case1 = a<=b
case2 = b>=a
print(case1 and case2)
case1 = a>=b
case2 = a<=b
print(case1 and case2)
#true lane  ke liye ## and operator me  dono ka true hona jaruri hai
# lakin ## or operator ke liye  ak bhi true ho to ho jayega
#| not operator
print(not False)
print(not True)
a = 50
b = 20
print(not a >= b)

