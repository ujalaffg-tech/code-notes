
#| Given an integer array nums and an integer target, 
#| return the indices of the two numbers such that they add
#| up to target. You may assume that exactly one valid answer exists,
#| and you may not use the same element twice. Return the answer in any order.

nums = [2,7,11,15]
def check(x):
    target = 12
    hashmap = {}
    n = len(x)
    for i in range(0,n):
        hashmap[x[i]]=i
    for j in range(0,n):
        if target-x[j] in hashmap and hashmap[target-x[j]] != j:
            return [j,hashmap[target-x[j]]]
print(check(nums))

#: T.C = O(N)
#: S.C = O(N)