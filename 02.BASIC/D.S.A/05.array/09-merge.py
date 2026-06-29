
#| Merge 2 Sorted Arrays Without Duplicates - 
nums1 = [1,1,1,2,4,5,5,6]
nums2 = [1,2,2,3,6,6,7,9]
def merge(x,y):
    list = []
    p = 0
    q = 0
    m = len(x)
    n = len(y)
    while p<m and q<n:
        if x[p]<=y[q]:
            if len(list)==0 or list[-1]!=x[p]:
                list.append(x[p])
            p+=1
        else:
            if len(list)==0 or list[-1]!=y[q]:
                list.append(x[q])
            q+=1
    while p<m:
        if list[-1]!=x[p]:
            list.append(x[p])
        p+=1
    while q<n:
        if list[-1]!=y[q]:
            list.append(y[q])
        q+=1
    return list
print(merge(nums1,nums2))