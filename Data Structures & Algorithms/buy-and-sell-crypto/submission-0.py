class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        if N == 1:
            return 0
        maxP = 0
        l = 0
        r = 1
        while l < N and r < N:
            if prices[r] < prices[l]:
                l = r
            if prices[r] > prices[r - 1]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            r += 1
        return maxP
            