class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in range(len(nums)):
            current_abs = abs(nums[i])
            if nums[current_abs - 1] < 0:
                res.append(current_abs)
            else:
                nums[current_abs - 1] *= -1

        return res
    

# Time complexity: O(n)
# Space complexity: O(1)