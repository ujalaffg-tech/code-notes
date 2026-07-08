
#| Longest Consecutive Sequence - 
nums = [1,99,101,98,2,5,3,100,1,1]
def check(x):
    n = len(x)
    count = 0
    result = 0
    for val in x:
        count = 1
        while val+1 in x:
            count+=1
            val+=1
        result = max(count,result)
    return result
print(check(nums))