
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