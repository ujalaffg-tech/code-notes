
#|1 ✅
n= [5,3,2,2,1,5,5,7,5,10] 
m= [10,111,1,9,5,67,2]
dict = {}
for val in n:
    dict[val]=dict.get(val,0)+1
for i in m:
    if i in dict:
        print(i,"-",dict[i])
    else:
        print(i,"-",0) 
#|2
d = [2,3,4,5,3,4,2,34,4,3]
dict = {}
for i in range(len(d)):
    dict[d[i]] = dict.get(d[i],0)+1
print(dict)
#|3
n= [5,3,2,2,1,5,5,7,5,10] 
m= [10,111,1,9,5,67,2]
dict = {}
for i in range(len(m)):
    dict[m[i]]=0
    for j in range(len(n)):
        if n[j] == m[i]:
            dict[m[i]]+=1
print(dict)
#|4
d = [5,3,2,2,1,5,5,7,5,10] 
dict = {}
for val in d:
    dict[val] = 0
for i in range(len(d)):
    dict[d[i]] += 1
print(dict)
#|5
n= [5,3,2,2,1,5,5,7,5,10] 
m= [10,111,1,9,5,67,2]
dict = {}
for val in m:
    count = 0
    for i in range(len(n)):
        if n[i] == val:
            count+=1
    print(val,"-",count)