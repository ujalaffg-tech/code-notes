
#| Find the Largest Element in an Array - 
nums = [55,32,-97,99,3,67]
def large(x):
    largest_no = float("-inf")
    for val in x:
        largest_no = max(val,largest_no)
    return largest_no
print(large(nums))

