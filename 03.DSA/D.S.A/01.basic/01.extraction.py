
#| digit extraction
n = 7395
while n>0:
    val= n%10
    print(val)
    n//=10

#.  T.C =  O(LOG N)
#.  S.C = O(1)

#| count digit
n = 5678
count = 0
while n>0:
    n//=10
    count +=1
print(count)

#.  T.C = O(LOG N)
#.  S.C = O(1)

#| count digit
num = 44545
from math import log10
if num>=0:
    if num == 0:
        print(1)
    else:
        print(int(log10(num)) + 1)
else:
    print("none")
    
#.  T.C = O(1)
#.  S.C = O(1)
 
#| palindrome 
num = 1221
result = 0
n = num
while n>0:
    val = n%10
    result = result * 10 + val
    n//=10
print(result==num)

#.  T.C = O(LOG N)
#.  S.C = O(1)

#| Armstrong number
num = 153
n = num
l = len(str(n))
result = 0
while n>0:
    val = n%10
    result = result + val**l
    n//=10
print(result==num)

#.  T.C = O(LOG N)
#.  S.C = O(1)

#| factor
n = 36
for i in range(1,n+1):
    if n%i == 0:
        print(i)

#. T.C = O(N)
#. S.C = O(1)

#| method 2
n = 36
for i in range(1,int((n/2)+1)):
    if n%i == 0:
        print(i)
print(n)

#. T.C = O(N/2)
#. S.C = O(1)

#| optimal method
n = 36
result = []
from math import sqrt
for i in range(1,int(sqrt(n)+1)):
    if n%i == 0:
        result.append(i)
        if n//i != i:
            result.append(n//i)
result.sort()
print(result)

#. T.C = O(√N)
#. S.C = O(K) where K = number of factors of N