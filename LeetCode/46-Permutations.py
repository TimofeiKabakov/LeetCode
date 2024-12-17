class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(permutation):
            if len(permutation) == len(nums):
                res.append(permutation)
                return
            
            for i in range(0, len(nums)):
                if nums[i] not in permutation:
                    dfs(permutation + [nums[i]])

        dfs([])
        
        return res
    
# Time Complexity: O(n! * n)
# Space Complexity: O(n)