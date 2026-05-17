
## digit extraction
#: print digit one by one
n = 7395
while n>0:
    val= n%10
    n//=10
    print(val)

## count digit
n = 5678
count = 0
while n>0:
    n//=10
    count +=1
print(count)


## count digit
num = 56789
from math import log10
if num == 0:
    print(1)
else:
    print(int(log10(num)) + 1)

## palindrome 
num = 1221
n = num
x = 0
while n>0:                                              #| code 💦
    val = n%10
    x = x * 10+ val
    n //=10
print(num == x)

## Armstrong number
num = 153
l= len(str(num))
n = num 
x = 0 
while n>0:                                              #| code 💦
    val = n%10
    x += val ** l
    n //= 10
print(x == num)

## factor
n = 15
list = []
for val in range(1,n+1):
    if(n % val == 0):
        list.append(val)
print(list)

## method 2
n = 15
list = []
for val in range(1,int(n/2)+1):
    if(n % val ==0):
        list.append(val)
list.append(n)
print(list)

## optimal method
from math import sqrt
n = 36
list = []
for val in range(1,int(sqrt(n))+1):
    if(n % val==0):
        list.append(val)
        if(n//val != val):
            list.append(n//val)
list.sort()
print(list)

