class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda i : i[0])
        ans = [intervals[0]]
        for start,end in intervals[1:]:
            lastend = ans[-1][1]

            if start<= lastend:
                #merge
                ans[-1][1] = max(end,lastend)
            else:
                ans.append([start,end])
        return ans