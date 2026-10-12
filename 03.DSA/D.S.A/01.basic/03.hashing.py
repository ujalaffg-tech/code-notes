
#|1
m= [5,3,2,2,1,5,5,7,5,10] 
n= [10,111,1,9,5,67,2]
def check(x,y):
    hash_list = [0]*11
    for val in x:
        hash_list[val]+=1
    for val2 in y:
        if val2>=0 and val2<=10:
            print(val2,"-",hash_list[val2])
        else:
            print(val2,"-",0)
check(m,n)

#. T.C = O(M+N)
#. S.C = O(1)

#|2
m = "aA12baaB22cC3A222A3dD43eE5QAf2F6"
n = ["a", "b", "2", "A", "e", "3"]
def check(x,y):
    lower_hash = [0]*26
    upper_hash = [0]*26
    digit_hash = [0]*10
    for val in x:
        if val.islower():
            lower_hash[ord(val)-ord('a')]+=1
        elif val.isupper():
            upper_hash[ord(val)-ord('A')]+=1
        else:
            digit_hash[ord(val)-ord('0')]+=1
    for val2 in y:
        if val2.islower():
            print(val2,"-",lower_hash[ord(val2)-ord('a')])
        elif val2.isupper():
            print(val2,"-",upper_hash[ord(val2)-ord('A')])
        else:
            print(val2,"-",digit_hash[ord(val2)-ord('0')])
check(m,n)

#. T.C = O(M+N)
#. S.C = O(1)