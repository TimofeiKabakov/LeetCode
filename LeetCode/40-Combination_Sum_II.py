class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def find_combinations(index, combo, current_sum):
            if current_sum == target:
                res.append(combo)
                return
            elif index == len(candidates):
                return

            find_combinations(index + 1, combo + [candidates[index]], current_sum + candidates[index])

            while index < len(candidates) - 1 and candidates[index + 1] == candidates[index]:
                index += 1
            find_combinations(index + 1, combo, current_sum)

        find_combinations(0, [], 0)

        return res
    
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n)