
#| Two Sum Problem (optimal solution)
nums = [6]
def check(x):
    target = 12
    hashmap = {}
    n = len(x)
    for i in range(0,n):
        hashmap[x[i]]=i
    for j in range(0,n):
        if target-x[j] in hashmap and hashmap[target-x[j]] != j:
            return [j,hashmap[target-x[j]]]
print(check(nums))
