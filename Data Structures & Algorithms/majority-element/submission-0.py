class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        map = {}

        for i in range(len(nums)):
            map[nums[i]] = 1 + map.get(nums[i],0)

        return max(map,key = map.get)