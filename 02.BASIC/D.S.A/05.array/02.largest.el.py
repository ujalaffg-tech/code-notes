
#| Find the Largest Element in an Array - 
nums = [55,32,-97,99,3,67]
def large(x):
    largest_no = float("-inf")
    for val in x:
        largest_no = max(val,largest_no)
    return largest_no
print(large(nums))

#-✅ Find the Largest Element in an Array - 
nums = [55,32,-97,99,3,67]
def largest_el(x):
    for i in range(len(x)-1):
        if x[i]>x[i+1]:
            x[i],x[i+1]=x[i+1],x[i]
    return x[len(x)-1]
print(largest_el(nums))