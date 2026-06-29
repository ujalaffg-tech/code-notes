
#| Check if an Array is Sorted - 
nums = [16,34,56,78,90]
def check(x):
    for i in range(len(x)-1):
        if x[i]>x[i+1]:
            return False
    return True
print(check(nums))
           

