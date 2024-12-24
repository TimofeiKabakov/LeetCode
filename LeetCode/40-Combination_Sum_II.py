class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(cur_ind, cur_sum, cur):
            if cur_sum == target:
                res.append(cur)
                return
            elif cur_sum > target or cur_ind == len(candidates):
                return

            new_ind = cur_ind
            while new_ind < len(candidates) - 1 and candidates[new_ind] == candidates[new_ind + 1]:
                new_ind += 1
            
            dfs(cur_ind + 1, cur_sum + candidates[cur_ind], cur + [candidates[cur_ind]])
            dfs(new_ind + 1, cur_sum, cur)

        dfs(0, 0, [])

        return res
    
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n)