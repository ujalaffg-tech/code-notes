
#| merge sort for assending order
nums = [3,1,2,4,1,5,2,6,4]
def merge_sort(x):
    if len(x)<=1:
        return x
    mid = len(x)//2
    left_half = x[:mid]
    right_half = x[mid:]
    left_half= merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half,right_half)
def merge(left,right):
    x,y=0,0
    m,n=len(left),len(right)
    result = []
    while x<m and y<n:
        if left[x]<=right[y]:
            result.append(left[x])
            x+=1
        else:
            result.append(right[y])
            y+=1
    if x<m :
        while x<m:
            result.append(left[x])
            x+=1
    if y<n:
        while y<n:
            result.append(right[y])
            y+=1
    return result
print(merge_sort(nums))

#| merge sort for dessending order
nums = [3,1,2,4,1,5,2,6,4]
def merge_sort(x):
    if len(x)<=1:
        return x
    mid = len(x)//2
    left_half = x[:mid]
    right_half = x[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return sort(left_half,right_half)
def sort(left,right):
    m,n = len(left),len(right)
    x,y = 0,0
    result = []
    while m>x and n>y:
        if left[x]>=right[y]:
            result.append(left[x])
            x+=1
        else:
            result.append(right[y])
            y+=1
    result.extend(left[x:])
    result.extend(right[y:])
    return result
print(merge_sort(nums))

