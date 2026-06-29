
#| Two Sum Problem
nums = [5,9,1,2,4,15,6,3]
def check(x):
    target = 13
    n = len(x)
    for i in range(0,n-1):
        for j in range(i,n):
            if x[i]+x[j]==target:
                return [i,j]
print(check(nums))

#| Two Sum Problem (optimal solution)
nums = [5,9,1,2,4,15,6,3]
def check(x):
    target = 13
    dict = {}
    n = len(x)
    for i in range(0,n):
        if (target - x[i]) in dict:
            return [dict[target-x[i]],i]
        dict[x[i]]=i
print(check(nums))

