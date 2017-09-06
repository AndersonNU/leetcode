# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.

# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
#
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

# Input: [7, 6, 4, 3, 1]
# Output: 0
#
# In this case, no transaction is done, i.e. max profit = 0.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxPro = 0
        minPrice = float('inf')
        for price in prices:
            minPrice = min(minPrice, price)
            maxPro = max(maxPro, price - minPrice)
        return maxPro

prices = [7, 1, 5, 3, 6, 4]
object = Solution()
print(object.maxProfit(prices))
