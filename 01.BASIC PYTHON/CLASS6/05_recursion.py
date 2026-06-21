def find_fact(x):
    if(x == 0 ):##this is called base case
        return 1
    else:
        return x * find_fact(x-1)
print(find_fact(5))

#- Write a recursive function to calculate the sum of first n natural numbers.
def sum(x):
    if(x  == 1):
        return 1
    else:
        return x + sum(x-1)
                  #: function ke ander funcutin name mtlb recursion
print(sum(5))


