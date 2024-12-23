class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        counter = 0
        intervals.sort()
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                counter += 1
                prevEnd = min(prevEnd, end)

        return counter


# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         counter = 0
#         intervals.sort(key = lambda interval: interval[0])
#         current = intervals[0]

#         for interval in intervals[1:]:
#             if current[0] <= interval[0] and current[1] > interval[0]:
#                 counter += 1
#                 if interval[1] > current[1]:
#                     continue
#             current = interval

#         return counter
    
# Time Complexity: O(nlogn)
# Space Complexity: O(1)