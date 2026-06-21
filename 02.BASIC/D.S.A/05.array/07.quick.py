nums = [2,3,4,3,3,23,4,4,322]
check = 4
def findd(x):
    for i in range(len(x)):
        if x[i]==check:
            return i
    return -1
print(findd(nums))