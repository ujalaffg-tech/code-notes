

#| Find the Second Largest Element in an Array -
nums = [100,66,777,101,67,87,98,34,16]
def check(x):
    

    largest = float("-inf")
    s_largest = float("-inf")
    for val in x:
        largest = max(largest,val)
        if val!=largest and val>s_largest:
            s_largest = val
    return s_largest
print(check(nums))