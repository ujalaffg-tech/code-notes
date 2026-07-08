
#| Find the Maximum Subarray Sum - (kadane's algorithm) - (optimal solution)  
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
    if result == float("-inf"):
        return None
    return result
print(check(nums))