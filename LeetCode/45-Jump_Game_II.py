# BFS approach
class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            count += 1

        return count

# Time Complexity: O(n)
# Space Complexity: O(1)

# DP approach
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        cur_min = [-1 for i in range(len(nums))]
        cur_min[len(nums) - 1] = 0

        for i in range(len(nums) - 2, -1, -1):
            step_min = 1000000
            for j in range(1, nums[i] + 1):
                if i + j < len(nums) and cur_min[i + j] != -1 and step_min > cur_min[i + j] + 1:
                    step_min = cur_min[i + j] + 1
            cur_min[i] = step_min

        return cur_min[0]
    
# Time Complexity: O(n^2)
# Space Complexity: O(n)