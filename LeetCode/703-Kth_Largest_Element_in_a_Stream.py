# Min heap solution
import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = nums
        self.k = k
        for i in range(len(nums) - k):
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]

# Time Complexity: O(n logk)
# Space Complexsity: O(n)        


# Max heap solution - not efficient time complexity
# because of popping and adding max elements back in the heap
# import heapq
# class KthLargest:
#     def __init__(self, k: int, nums: List[int]):
#         nums_negative = [-1 * n for n in nums]
#         heapq.heapify(nums_negative)
#         self.heap = nums_negative
#         self.k = k

#     def add(self, val: int) -> int:
#         heapq.heappush(self.heap, -1 * val)

#         counter = 0
#         nums_popped = []
#         while(counter != self.k):
#             largest = heapq.heappop(self.heap)
#             nums_popped.append(largest)
#             counter += 1
        
#         for n in nums_popped:
#             heapq.heappush(self.heap, n)

#         return -1 * largest
        
