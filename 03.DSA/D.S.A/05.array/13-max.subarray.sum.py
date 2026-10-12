
#| Given an integer array nums, find the contiguous subarray
#| (containing at least one element) that has the largest sum, 
#| and return that sum.
  
nums = [-2,1,-3,4,-1,2,1,-5,4]
def check(x):
    n = len(x)
    count = 0
    result = float("-inf")
    for i in range(0,n):
        count+=x[i]
        result = max(count,result)
        if count<0:
            count=0
    return result
print(check(nums))

#: T.C = O(N)
#: S.C = O(1)
