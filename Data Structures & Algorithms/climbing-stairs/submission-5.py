class Solution:
    def climbStairs(self, n: int) -> int:
        

        # def dfs(i):
        #     if i ==n:
        #         return 1
        #     elif i > n:
        #         return 0

        # return dfs(0)

        #below use Memoization 
        #Below method is top down method(dfs) 
        
        # memo = {}

        # def dfs(i):
        #     if i ==n:
        #         return 1
        #     elif i > n:
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     memo[i] = dfs(i+1) + dfs(i+2)

        #     return memo[i]
        # return dfs(0)


        # below method is bottom up 
        # dp = [0]* (n+1)

        # if n<=2:
        #     return n
        # dp[1], dp[2] = 1,2

        # for i in range(3,len(dp)):
        #     dp[i]= dp[i-1] + dp[i-2]
        # return dp[-1]

        #Below is the Actual DP solution.(Solution 4 in neetcode)
        #we basically start from the end of the array and keep computing backwards
        # till we reach the first value and then return that 

        one , two = 1,1

        for i in range(n-1):
            temp = one
            one = one+ two
            two = temp
        return one






















