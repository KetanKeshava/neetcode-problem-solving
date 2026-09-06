"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

#intervals = [(0,40),(5,10),(15,20)]

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)

        start.sort()
        end.sort()

        s = 0
        e = 0
        count = 0
        res = 0

        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            
            else:
                count -= 1
                e += 1
            
            res = max(res,count)
        
        return res






