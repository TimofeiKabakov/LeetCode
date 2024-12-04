class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda interval: interval.start)
        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False
        return True

# Time Complexity: O(n log n)
# Space Complexity: O(1)