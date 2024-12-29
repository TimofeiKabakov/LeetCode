class Solution:
    def canJump(self, nums: List[int]) -> bool:
        prev_ind = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= prev_ind:
                prev_ind = i

        return prev_ind == 0
    
# Time Complexity: O(n)
# Space Complexity: O(1)