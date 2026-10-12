
#| tail recursion - recursive call function ke last me ho 
def check(i, n):
    if i > n:
        return
    print(i)
    check(i + 1, n)
check(1, 5)

#| non tail recursion - resursive call ke bad bhi function me kuch kam bacha ho
def check(i, n):
    if i > n:
        return
    check(i + 1, n)
    print(i)
check(1, 5)

#| use of tail 
#= Jab answer jate waqt (going down) hi ban sakta hai.
#= Examples: 1 se N print

#| use of head
#=Jab answer wapas aate waqt (coming back) banana ho.
#= Examples: N se 1 print