
#| Given an integer array nums, return the second largest 
#| distinct element present in the array. If the array does not 
#| contain a second distinct largest element, return None.

nums = [50, 99, 30, 99]
def check(x):
    largest = float("-inf")
    s_largest = float("-inf")

    for val in x:
        if val>largest:
            s_largest = largest
            largest = val

        elif val!=largest and val>s_largest:
            s_largest = val

    if s_largest == float("-inf"):
        return None
    return s_largest

print(check(nums))

#. T.C = O(N)
#. S.C = O(1)
