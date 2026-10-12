
#| You are given a sorted integer array nums.
#| Remove the duplicate elements in-place such that each unique
#| element appears only once. Return the number of unique elements k.
#| The first k elements of nums should contain the unique elements in their 
#| original sorted order. The remaining elements of the array do not matter.
nums = [1,1,2,2,3,3,4,4,4,5,5,6,6,6,7]
def check(x):
        if len(x)<=0:
             return 0
        i = 0
        j = 1
        while j<len(x):
            if x[i] != x[j]:
                x[i+1],x[j]=x[j],x[i+1]
                i+=1
            j+=1
        return i+1
print(check(nums))
print(nums)

#. T.C = O(N)
#. S.C = O(1)

#- Given a sorted integer array nums, remove duplicate elements
#- and keep only the unique elements in the array.
#- Return the number of unique elements.
#- The first k elements of nums should contain the unique elements.

nums = [1,1,2,2,3,3,4,4,4,5,5,6,6,6,7]
def check(x):
    hashmap = {}
    for val in x:
        hashmap[val]=0
    j = 0
    for k in hashmap:
        x[j]=k
        j+=1
    return j
print(check(nums))
print(nums)

#. T.C = O(N + K)
#. S.C = O(K) where k = number of unique element in x
