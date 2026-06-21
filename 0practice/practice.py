
nums=[1,0,3,4]
def check(x):
    n = len(x)
    i = 0
    for val in x:
        i+=val
    return int(n*(n+1)/2)-i
print(check(nums))

