
#| Best Time to Buy and Sell Stock - (optimal solution)
prices = [1]
def check(x):
    miniidx = float("inf")
    max_profit = 0
    n = len(x)
    for i in range(0,n):
        miniidx = min(miniidx,x[i])
        max_profit = max(max_profit,x[i]-miniidx)
    return max_profit
print(check(prices))