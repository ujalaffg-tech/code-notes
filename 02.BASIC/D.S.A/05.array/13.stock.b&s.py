
#| Best Time to Buy and Sell Stock - (brute force solution)
prices = [7,2,1,5,6,4,8]
def check(x):
    n = len(x)
    max_profit = 0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if x[i]<x[j]:
                var = x[j]-x[i]
                max_profit = max(max_profit,var)
    return max_profit
print(check(prices))

#| Best Time to Buy and Sell Stock - (optimal solution)
prices = [7,2,1,5,6,4,8]
def check(x):
    n = len(x)
    min_price = float("inf")
    max_profit = 0
    for i in range(0,n):
        min_price = min(min_price,x[i])
        max_profit = max(max_profit,(x[i]-min_price))
    return max_profit
print(check(prices)) 
