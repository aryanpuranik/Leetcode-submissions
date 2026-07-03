class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # O(n2)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        # return False



        # O(2N)

        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         return True
        # return False



        # O(N)
        map = {}

        for i in nums:
            if i in map:
                return True
            map[i]= True 
        return False