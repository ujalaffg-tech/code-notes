
#| Given an integer array nums and an integer target,
#| return the index of the first occurrence of target in the array.
#| If the target is not present in the array, return -1.

nums = [1,2,3,4,3]
def findd(x,target):
    
    for i in range(len(x)):
        if x[i]==target:
            return i
    return -1
print(findd(nums,4))

#: T.C = O(N)
#: S.C = O(1)