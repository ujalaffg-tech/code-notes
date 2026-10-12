
#| print 1 to n using tail recursion
def func(x,n):
    if x>n:
        return
    print(x)
    func(x+1,n)
func(1,15)
#. T.C = 0(N)
#. S.C = 0(N)

#| print 1 to n using head recursion
def func(x):
    if x==0:
        return 
    func(x-1)
    print(x)
func(5)

#. T.C = 0(N)
#. S.C = 0(N)

#| using parametrized recursion  sum 1 to n.
def func(sum,i,n):
    if i>n:
        print(sum)
        return
    func(sum+i,i+1,n)
func(0,1,5)
#. T.C = 0(N)
#. S.C = 0(N)


#|🫆 functional recursion
def func(n):
    if n==1:
        return 1
    return n + func(n-1)
func(5)
#. T.C = 0(N)
#. S.C = 0(N)

#|🫆 find factorial
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
print(fact(5))
#. T.C = 0(N)
#. S.C = 0(N)

#-1 reverse array using to recursion
num = [5,7,3,2,6,1,5,9]
def func(arrs,left,right):
    if left>=right:
        return
    arrs[left],arrs[right]=arrs[right],arrs[left]
    return func(arrs,left+1,right-1)
func(num,0,(len(num)-1))
print(num)
#. T.C = 0(N/2)
#. S.C = 0(N/2)

#- loop se
n = [5,7,3,2,6,1,5,9]
def func(num):
    left= 0
    right = (len(num)-1)
    while left<right:
        num[left],num[right]=num[right],num[left]
        left+=1
        right-=1
    print(n)
func(n)
#. T.C = 0(N/2)
#. S.C = 0(1)

#-2 num = [5,7,1,6,2,3,5,9]
num = [5,7,3,2,6,1,5,9]
def func(arrs,left,right):
    if left>=right:
        return
    arrs[left],arrs[right]=arrs[right],arrs[left]
    return func(arrs,left+1,right-1)
func(num,2,5)
print(num)
#. T.C = 0(right-left)
#. S.C = 0(right-left)

#-3 check palindrome using to recursion
n = "adad"
def check(x,a,left,right):
    if left>right:
        return  a == "".join(x)
    x[left],x[right]=x[right],x[left]
    return check(x,a,left+1,right-1)
print(check(list(n),n,0,len(n)-1))
#. T.C = 0(N/2)
#. S.C = 0(N/2)

#- loop se
word = "nitin"
def check(h):
    x = list(h)
    left = 0
    right = (len(x)-1)
    while left<=right:
        x[left],x[right]=x[right],x[left]
        left+=1
        right-=1
    print(h=="".join(x))
check(word)
#. T.C = 0(N/2)
#. S.C = 0(N)

#- check pallindrome for digit
num = 121445
x = list(str(num))
left = 0
right = len(x)-1
while left<right:
    x[left],x[right]=x[right],x[left]
    left+=1
    right-=1
print("".join(x)==str(num))
#. T.C = 0(N/2)
#. S.C = 0(N) 
#: naya list bana isliye S.C 0(N) varna 0(1) hota
