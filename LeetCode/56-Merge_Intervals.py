def is_overlapping(interval1, interval2):
    return interval1[1] >= interval2[0]

def merge_intervals(interval1, interval2):
    min_val = min(interval1[0], interval2[0])
    max_val = max(interval1[1], interval2[1])
    return [min_val, max_val]

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval: interval[0])
        result = [intervals[0]]
        
        for interval in intervals[1:]:
            if is_overlapping(result[-1], interval):
                interval2 = result.pop()
                merge_interval = merge_intervals(interval, interval2)
                result.append(merge_interval)
            else:
                result.append(interval)

        return result