
## digit extraction
#: print digit one by one
n = 7395
while n>0:
    val= n%10
    n//=10
    print(val)
#.  T.C = 0(LOG N)
#.  S.C = 0(1)

## count digit
n = 5678
count = 0
while n>0:
    n//=10
    count +=1
print(count)
#.  T.C = 0(LOG N)
#.  S.C = 0(1)

## count digit
num = 56789
from math import log10
if num == 0:
    print(1)
else:
    print(int(log10(num)) + 1)
#.  T.C = 0(1)
#.  S.C = 0(1)

## palindrome 
num = 1221
n = num
x = 0
while n>0:                                              #| code 💦
    val = n%10
    x = x * 10+ val
    n //=10
print(num == x)
#.  T.C = 0(LOG N)
#.  S.C = 0(1)
'''Kyun?
Time Complexity — O(log n):
Har iteration mein n //= 10 hota hai
Yaani n ke digits kitne hain = log₁₀(n) baar loop chalega
1221 ke 4 digits → 4 iterations → O(log n)

Space Complexity — O(1):
Sirf 3 variables use ho rahe hain: n, x, val
Koi extra array/list/string nahi bana
Input size badhne pe memory nahi badhti → O(1)'''

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
#.  T.C = 0(LOG N)
#.  S.C = 0(1)

## factor
n = 15
list = []
for val in range(1,n+1):
    if(n % val == 0):
        list.append(val)
print(list)
#. T.C = 0(N)
#. S.C = 0(1)

## method 2
n = 15
list = []
for val in range(1,int(n/2)+1):
    if(n % val ==0):
        list.append(val)
list.append(n)
print(list)
#. T.C = 0(N/2)
#. S.C = 0(1)

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
#. T.C = 0(N**2)
#. S.C = 0(1)