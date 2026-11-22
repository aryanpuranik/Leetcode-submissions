class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        res = []

        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]]= 0
            map[nums[i]]+=1
        count = sorted(map, key=map.get, reverse = True)
        for i in range(k):
            res.append(count[i])
        return res
            
