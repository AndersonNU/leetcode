# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions
# as you like (ie, buy one and sell one share of the stock multiple times). However,
# you may not engage in multiple transactions at the same time (ie, you must sell the
# stock before you buy again).

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        stocks = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i] and stocks is 0:
                profit = prices[i+1] - prices[i]
                stocks = 1
            if prices[i+1] < prices[i] and stocks is 1:
                profit = prices[i] - prices[i+1]
                stocks = 0
        return profit

    def buy(self):
        profit = prices[i+1] - prices[i]

    def sell(self):
        profit = prices[i] - prices[i+1]

prices = [1,2,3,6,7,9,11,8,5,3]
object = Solution()
print(object.maxProfit(prices))
