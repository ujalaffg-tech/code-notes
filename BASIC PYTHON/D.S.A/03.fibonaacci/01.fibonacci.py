
## fibonacci number
def func(num):
    if num==0 or num==1:
        return num
    return func(num-1)+func(num-2)
print(func(8))
## t.c = 0(2**n)
## s.c = 0(n)
