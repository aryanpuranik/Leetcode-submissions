"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        i = 0
        j = 0
        count = 0
        max_val = 0
        while i<len(intervals):
            if start[i]<end[j]:
                count+=1
                i+=1
                max_val = max(max_val,count)
            else:
                count -=1
                j+=1
            
        return max_val

