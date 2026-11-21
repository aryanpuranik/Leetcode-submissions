class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        map = {}

        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]]=0
            map[nums[i]]+=1
            if map[nums[i]]>1:
                return True
        return False