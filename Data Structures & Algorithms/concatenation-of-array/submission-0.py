class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # return nums+nums

        ans = [0] * (2*len(nums))
        for i in range(len(nums)):
            ans[i] = ans[i+len(nums)] = nums[i]
        return ans