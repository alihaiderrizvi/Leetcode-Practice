class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x:x[0])
        
        if len(intervals) < 2:
            return intervals
        
        merged = [intervals[0]]
        
        for time in intervals[1:]:
            if time[0] > merged[-1][1]:
                merged.append(time)
            else:
                merged[-1] = [min(merged[-1][0], time[0]), max(merged[-1][1], time[1])]
        return merged
