class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def dfs(cur, subset):
            if cur >= len(nums):
                res.append(subset)
                return
            
            dfs(cur + 1, subset + [nums[cur]])

            cur += 1
            while (cur < len(nums)) and (nums[cur] == nums[cur - 1]):
                cur += 1

            dfs(cur, subset)

        dfs(0, [])
        
        return res

# Time Complexity: O(n * 2^n)
# Space Complexity: O(n)

# DFS + Hash Map solution
# def compute_hash(subset):
#     count = [0] * 11
#     for element in subset:
#         count[element] += 1
#     return tuple(count)

# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         hash_map = {}

#         def dfs(cur, subset):
#             if cur == len(nums):
#                 hash_subset = compute_hash(subset)
#                 if hash_subset not in hash_map.keys():
#                     hash_map[hash_subset] = 1
#                     res.append(subset)
#                 return
            
#             dfs(cur + 1, subset)
#             dfs(cur + 1, subset + [nums[cur]])

#         dfs(0, [])

#         return res