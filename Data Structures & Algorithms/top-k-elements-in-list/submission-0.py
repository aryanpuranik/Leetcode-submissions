class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #create a dict - have the value and num , then
        count = {}
        res = []
        for i in range(len(nums)):
            count[nums[i]]=1 + count.get(nums[i],0)
        s_count = sorted(count, key=count.get)

        return s_count[-k:]
        # for i in range(len(s_count),-k):
        #     res.append(s_count[i])
        # return res

