class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen ={}

        for i,num in enumerate(nums):
            number = target - num
            if number in seen:
                return [seen[number], i]
            seen[num] = i
