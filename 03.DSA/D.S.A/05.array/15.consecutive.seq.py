
#- Given an unsorted integer array nums, return the length of
#- the longest consecutive sequence. A consecutive sequence consists of
#- numbers that follow each other by 1, regardless of their order in the array.
#- Your algorithm must run in O(n) time.

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

#| print 1 to n using tail recursion
n = 5
def check(x):
    if x==1:
        return 1
    check(x-1)
    print(x)
check(n)


