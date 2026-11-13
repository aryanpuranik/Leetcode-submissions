class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    
    #Using max heap 
        # heapq.heapify_max(nums)

        # res =0
        
        # while k>0:
        #     res = heapq.heappop_max(nums)
        #     k-=1
        # return res 

        #using min heap - slightly better time complexity

        minheap= []
        for i in nums:
            if len(minheap)<k:
                heapq.heappush(minheap,i)
            elif i > minheap[0]:
                heapq.heappop(minheap)
                heapq.heappush(minheap,i)
        return minheap[0]