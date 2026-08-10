class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for index, val in enumerate(nums):
            seen[val] = index
        for i in range(len(nums)):
            if target - nums[i] in seen and seen[target - nums[i]] != i:
                return [i,seen[target - nums[i]]]