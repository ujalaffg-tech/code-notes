
#| Given an integer array nums, return the largest element
#| present in the array. If the array is empty, return None.

nums = [55,32,-97,99,3,67]
def large(x):
    if len(x)==0:
        return None
    largest_no = float("-inf")
    for val in x:
        largest_no = max(val,largest_no)
    return largest_no
print(large(nums))

#. T.C = O(N)
#. S.C = O(1)
