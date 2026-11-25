class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for buy in range(len(prices)):
            for sell in range(buy+1,len(prices)):
                ans = max(prices[sell]-prices[buy],ans)
        return ans