# Question : You are given an array prices where prices[i] is the price of a given stock on the ith day.You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Approach : I tracked the minimum buying price so far and calculated the maximum profit at each step in a single traversal.
# Time Complexity : O(n)\
# Space Complexity : O(1)


def maxProfit(self, prices: List[int]) -> int:
        buyStock = prices[0]
        maxGain = 0

        for i in range(len(prices)):
            if prices[i]<buyStock:
                buyStock = prices[i]
            else:
                Gain = prices[i]-buyStock
                maxGain = max(maxGain , Gain)
        return maxGain
