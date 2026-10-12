
#| Given a binary array nums (an array containing only 0s and 1s),
#| return the maximum number of consecutive 1s in the array.

nums = [1,1,0,1,0,1,1,1,1,0,1,1]
def check(x):
    result = 0
    count = 0
    for i in range(0,len(x)):
        if x[i]==1:
            count+=1
            result = max(result,count)
        else:
            count = 0
    return result
print(check(nums))

#: T.C = O(N)
#: S.C = O(1)