class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #O(n2)
        # ans = nums[0]
        # for i in range(len(nums)):
        #     suma= 0
        #     for j in range(i,len(nums)):
        #         suma += nums[j]
        #         ans = max(suma,ans)
        # return ans


        cursum = 0
        maxsub = nums[0]

        for i in nums:
            if cursum <0:
                cursum = 0
            cursum+=i
            maxsub = max(cursum, maxsub)
        return maxsub