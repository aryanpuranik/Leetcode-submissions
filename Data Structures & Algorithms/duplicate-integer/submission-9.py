class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        sett = set()

        for n in range(len(nums)):
            if nums[n] in sett:
                return True

            sett.add(nums[n])
        return False