def merge_intervals(interval1, interval2):
    min_start = min(interval1[0], interval2[0])    
    max_start = max(interval1[1], interval2[1])    
    return [min_start, max_start]

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):
            interval = intervals[i]
            if newInterval[1] < interval[0]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            elif newInterval[0] > interval[1]:
                result.append(interval)
            else:
                newInterval = merge_intervals(interval, newInterval)

        result.append(newInterval)

        return result
    
# Time Complexity: O(n)
# Space Complxity: O(n)