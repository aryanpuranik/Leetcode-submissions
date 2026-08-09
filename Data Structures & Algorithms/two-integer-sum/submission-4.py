class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for index,val in enumerate(nums):
            
            find = target - val
            if find in seen:
                return[seen[find],index]
            seen[val] = index
