"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        max_counter, counter, start_pointer, end_pointer = 0, 0, 0, 0

        start_times = [interval.start for interval in intervals]
        end_times = [interval.end for interval in intervals]
        start_times.sort()
        end_times.sort()

        while(start_pointer != len(intervals) and end_pointer != len(intervals)):
            if start_times[start_pointer] < end_times[end_pointer]:
                start_pointer += 1
                counter += 1
                if counter > max_counter:
                    max_counter = counter
            else:
                end_pointer += 1
                counter -= 1

        return max_counter
