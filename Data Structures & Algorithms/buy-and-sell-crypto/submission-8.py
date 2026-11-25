class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n2)
        # ans = 0
        # for buy in range(len(prices)):
        #     for sell in range(buy+1,len(prices)):
        #         ans = max(prices[sell]-prices[buy],ans)
        # return ans

        #O(n)

        buy = 0
        sell = 1
        ans = 0
        while sell<len(prices):
            ans = max(prices[sell] - prices[buy],ans)
            if prices[sell]<prices[buy]:
                buy = sell
            # else:
            #     ans = max(prices[sell] - prices[buy],ans)
            sell+=1
        return ans

                

              
