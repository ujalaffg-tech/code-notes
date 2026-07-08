
## fibonacci number
def func(n):
    if n==0 or n==1 :
        return n
    return func(n-1)+func(n-2)
print(func(8))
#. T.C = 0(2**N)
#. S.C = 0(N)
