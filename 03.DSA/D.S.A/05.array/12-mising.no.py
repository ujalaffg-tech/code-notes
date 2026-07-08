
#|1 Find Missing Number in an Array -
nums=[1,0,3,4]
def check(x):
    n = len(x)
    i = 0
    for val in x:
        i+=val
    return int(n*(n+1)/2-i)
print(check(nums))

#- Find Missing Number in an Array -
nums=[17,4,6,3,1,2,4,0]
def check(x):
    n = len(x)
    hashmap = {}
    for i in range(0,n+1):
        hashmap[i] = 0
    for j in range(0,n):
        hashmap[x[j]] = 1
    for k,v in hashmap.items():
        if v==0:
            return k
print(check(nums))

#-3 Find Missing Number in an Array - worst case 
nums=[1,0,3,4]
def check(x):
    n = len(x)
    for i in range(0,n+1):
        if i not in x:
            return i
print(check(nums))
