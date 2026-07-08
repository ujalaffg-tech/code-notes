
#| Merge 2 Sorted Arrays Without Duplicates - 
nums1 = [1,1,1,2,4,5,5,6]
nums2 = [1,2,2,3,6,6,7,9]

def check(x,y):
    i = 0
    j = 0
    m = len(x)
    n = len(y)
    result = []

    while i<m and j<n:
        if x[i]<=y[j]:
            if len(result)==0 or result[-1]!=x[i]:
                result.append(x[i])
            i+=1

        else:
            if len(result)==0 or result[-1]!=y[j]:
                result.append(y[j])
            j+=1

    while i<m:
        if len(result)==0 or result[-1]!=x[i]:
            result.append(x[i])
        i+=1

    while j<n:
        if len(result)==0 or result[-1]!=y[j]:
            result.append(y[j])
        j+=1
    return result

print(check(nums1,nums2))