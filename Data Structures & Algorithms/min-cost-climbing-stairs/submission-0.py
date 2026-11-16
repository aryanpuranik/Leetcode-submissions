class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        one = cost[-1]
        two = 0
        for i in range(len(cost)-2,-1,-1):
            temp = one
            one = min(cost[i]+one, cost[i] +two)
            two = temp
        return min(one,two)

