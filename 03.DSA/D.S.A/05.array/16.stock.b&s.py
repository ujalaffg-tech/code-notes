
#| Given an array prices where prices[i] is the price of a stock
#| on the iᵗʰ day, find the maximum profit you can achieve by buying one
#| stock and selling one stock. You must buy before you sell.
#| If no profit can be made, return 0.

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

#: T.C = O(N)
#: S.C = O(1)