
#|1 ✅
n= [5,3,2,2,1,5,5,7,5,10] 
m= [10,111,1,9,5,67,2]
dict = {}
for val in m:
    dict[val] = 0
for i in n:
    if i in dict:
        dict[i]+=1
print(dict)
#. T.C = 0(M+N)
#. S.C = 0(M)

#|2
d = [5,3,2,2,1,5,5,7,5,10]
dict = {}
for val in d:
    dict[val] = 0
for i in range(len(d)):
        dict[d[i]]+=1
print(dict)
#. T.C = 0(2*M) = 0(M)
#. S.C = 0(D)

#|3
n= [5,3,2,2,1,5,5,7,5,10] 
m= [10,111,1,9,5,67,2]
for val in m:
    count = 0
    for i in n:
        if i == val:
            count+=1
    print(val,"-",count)
#. T.C = 0(M*N)
#. S.C = 0(1)

#|4
n= [5,3,2,2,1,5,5,7,5,10] 
m= [10,111,1,9,5,67,2]
dict = {}
for val in n:
    dict[val] = dict.get(val,0)+1
for i in m:
    if i in dict:
        print(i,"-",dict[i])
    else:
        print(i,"-",0)
#. T.C = 0(M+N)
#. S.C = 0(N)

#|5
d = [5,3,2,2,1,5,5,7,5,10]
dict = {}
for val in d:
    dict[val] = dict.get(val,0)+1
print(dict)
#. T.C = 0(D)
#. S.C = 0(D)

'''Golden Rule:
Jab bhi Dictionary use ho → S.C hamesha O(N) hoga,
jahan N = stored elements ki count '''