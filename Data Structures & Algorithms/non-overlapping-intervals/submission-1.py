class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        res = 0
        prevend = intervals[0][1]

        for start, end in intervals[1:]:
            if prevend > start: #There is an overlap
                res +=1
                prevend= min(end,prevend)

            else: #No overlap
                prevend = end
        return res


