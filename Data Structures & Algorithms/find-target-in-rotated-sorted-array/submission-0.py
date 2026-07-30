class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l =0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if target==nums[mid]:
                return mid
            #left side

            if nums[mid] >=nums[l]:
                if target < nums[l] or target >nums[mid]:
                    l = mid+1
                else:
                    r = mid-1
            #right side
            
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid -1
                else:
                    l = mid+1
                
        return -1

            