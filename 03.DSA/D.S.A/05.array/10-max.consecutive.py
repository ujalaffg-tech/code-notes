
#| Max Consecutive Ones -
nums = [1,1,0,1,0,1,1,1,1,0,1,1]
def check(x):
    result = 0
    count = 0
    for i in range(0,len(nums)):
        if x[i]==1:
            count+=1
            result = max(result,count)
        else:
            count = 0
    return result
print(check(nums))