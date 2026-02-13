"""Best Time to Buy and Sell Stock"""

def maxProfit(prices):
    n = len(prices)
    minProfit = float("inf")
    maxProfit = 0
    for i in range(0,n):
        minProfit = min(minProfit,prices[i])
        maxProfit = max(maxProfit,prices[i] - minProfit)
    return maxProfit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))