class Solution:        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def find_subsets(subset, current_index):
            if current_index == len(nums):
                result.append(subset)
                return

            # Do not add current num to the subset and continue traversing
            find_subsets(subset[:], current_index + 1)

            # Add current num to the subset and continue traversing
            subset.append(nums[current_index])
            find_subsets(subset[:], current_index + 1)
        
        find_subsets([], 0)

        return result

# Time Complexity: O(n * 2^n)
# Space Complexity: O(n)