
#| Find the Maximum Subarray Sum - (wrost case)
nums = [-2,6,-3,4]
def check(x):
    n = len(x)
    result = float("-inf")
    for i in range(0,n):
        count = 0
        for j in range(i,n):
            count = count + x[j]
            result = max(count,result)
    return result
print(check(nums))

#| Find the Maximum Subarray Sum - (kadane's algorithm) - (optimal solution)  
nums = [-2,1,-3,4,-1,2,1,-5,4]
def check(x):
    n = len(x)
    result = float("-inf")
    count = 0
    for i in range(0,n):
        count = count+x[i]
        result = max(result,count)
        if count < 0:
            count = 0
    return result
print(check(nums))