class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval : interval[0])
        
        # Initialization
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            # check if last interval in output is overlapping with current interval
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else: 
                output.append([start,end])
        return output     