
#|1 Find Missing Number in an Array -
nums=[1,0,3,4]
def check(x):
    n = len(x)
    for i in range(0,n+1):
        if i not in x:
            return i
        
print(check(nums))

## Find Missing Number in an Array -
nums=[1,0,3,4]
def check(x):
    n = len(x)
    for i in range(0,n+1):
        if i in x:
            pass
        
        else:
            return i
print(check(nums))

#|2 Find Missing Number in an Array -
nums=[1,0,3,4]
def check(x):
    dict = {}
    n = len(x)
    for i in range(0,n+1):
        dict[i]=0
    for val in x:
        dict[val]+=1
    for k,v in dict.items():
        if v==0:
            return k
print(check(nums))

#|3 Find Missing Number in an Array -
nums=[1,0,3,4]
def check(x):
    n = len(x)
    i = 0
    for val in x:
        i+=val
    return int(n*(n+1)/2)-i
print(check(nums))


