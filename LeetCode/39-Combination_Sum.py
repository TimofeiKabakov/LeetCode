class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def find_combinations(cur, cur_sum, index):
            if cur_sum == target and cur not in res:
                res.append(cur)
                return
            elif cur_sum > target or index == len(nums):
                return

            # Do not add anything
            find_combinations(cur, cur_sum, index + 1)    

            # Add the most recent one
            new_combination = cur + [nums[index]]
            find_combinations(new_combination, cur_sum + nums[index], index)
        
            # Add next one
            if index + 1 < len(nums):
                new_combination = cur + [nums[index + 1]]
                find_combinations(new_combination, cur_sum + nums[index + 1], index + 1)

        find_combinations([], 0, 0)

        return res