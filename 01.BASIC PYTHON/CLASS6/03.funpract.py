
#- WAF to print the length of a list. (list is the parameter)
nums = [2,3,4,5,9]
cities= [ "patna", "delhi" , "mumbai"]
def len_of_list(x):
    print(len(x))
    return len(x)  #len(x) nahi bhi likhoge to ho jayega,
len_of_list(cities) 
len_of_list(nums)

#| WAF to print the elements of a list in a single line. (list is the parameter)
nums = [2,3,4,5,9]
cities= [ "patna", "delhi" , "mumbai"]
def print_list(x):
    for val in x:
        print(val,end=" ")
print_list(nums)
print()


#| WAF to print the elements of a list in a single line. (list is the parameter)
nums = [2,3,4,5,9]
cities= [ "patna", "delhi" , "mumbai"]
def print_el(x):
    idx = 0
    while idx < len(x):
        print(x[idx])
        idx+=1
    return x # while loop khatam hone ke bad ye kam kardega apna
print_el(nums)





