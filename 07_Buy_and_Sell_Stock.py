# Question : You are given an integer array prices where prices[i] is the price of a given stock on the ith day.On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.Find and return the maximum profit you can achieve.
# Approach : I use a greedy approach where I accumulate profit for every increasing pair of consecutive days, since multiple transactions are allowed.
# Time Complexity : O(n)
# Space Complexity : O(1)

def maxProfit(self, prices: List[int]) -> int:
        maxGain = 0
        for i in range (1,len(prices)):
            if prices[i]> prices[i-1]:
                maxGain += prices[i]- prices[i-1]
        
        return maxGain
