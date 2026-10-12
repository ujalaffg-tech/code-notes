
#|1
m= [5,3,2,2,1,5,5,7,5,10] 
n= [10,111,1,9,5,67,2]
def check(x,y):
    hashmap = {}
    for val in x:
        hashmap[val]=hashmap.get(val,0)+1
    for val2 in y:
        print(val2,"-",hashmap.get(val2,0))
check(m,n)

#. T.C = O(M+N) 
#. S.C = O(K), where K = number of unique elements in x.

#|2
m= [5,3,2,2,1,5,5,7,5,10] 
n= [10,111,1,9,5,67,2]
def check(x,y):
    hashmap= {}
    for val in y:
        hashmap[val]=0
    for val2 in x:
        if val2 in dict:
            hashmap[val2]+=1
    return hashmap
print(check(m,n))

#. T.C = O(M+N)
#. S.C = O(N)

#|3
m= [5,3,2,2,1,5,5,7,5,10] 
n= [10,111,1,9,5,67,2]
def check(x,y):
    for val in y:
        count = 0
        for val2 in x:
            if val2 == val:
                count+=1
        print(val,"-",count)
check(m,n)

#. T.C = O(M * N)
#. S.C = O(1)



