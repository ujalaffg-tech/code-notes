
#| Find the Second Largest Element in an Array -
nums = [100,66,777,101,67,87,98,34,16]
def large(x):
    largest = float("-inf")
    s_largest = float("-inf")
    for val in x:
        if val>largest:
            s_largest = largest
            largest = val
        elif s_largest<val and val!=largest:
            s_largest = val
    return s_largest
print(large(nums))

#-✅ Find the Second Largest Element in an Array -
nums = [100,66,777,67,87,98,34,16]
def large(x):
    largest = float("-inf")
    s_largest = float("-inf")
    for val in x:
        if val>largest:
            largest = val
    for val in x:
        if val<largest and val>s_largest:
            s_largest = val
    return s_largest
print(large(nums))



