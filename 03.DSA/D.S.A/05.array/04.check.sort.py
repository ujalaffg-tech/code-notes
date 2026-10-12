
#| Given an integer array nums, determine whether the array 
#| is sorted in non-decreasing order.

nums = [16,16,56,78,90]
def check(x):
    for i in range((len(x)-1)):
        if x[i]>x[i+1]:
            return "False"
    return "True"
print(check(nums))

#. T.C = O(N)
#. S.C = O(1)


