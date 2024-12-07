import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-1 * stone for stone in stones]
        heapq.heapify(max_heap)
        
        while(len(max_heap) > 1):
            first_largest = -1 * heapq.heappop(max_heap)
            second_largest = -1 * heapq.heappop(max_heap)
            if first_largest != second_largest:
                new_val =  -1 * abs(first_largest - second_largest)
                heapq.heappush(max_heap, new_val)

        if not len(max_heap):
            return 0

        return -1 * max_heap[0]

# Time Complexity: O(n log n)
# Space Complexity: O(n)