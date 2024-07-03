class Solution:
    def search(self, nums: List[int], target: int) -> int:
            def binary_search(nums: List[int], left_i: int, right_i: int) -> int:
                if left_i == right_i and nums[0] == target:
                    return left_i
                elif left_i == right_i:
                    return -1
                
                middle = len(nums) // 2
                leftPart = nums[0 : middle]
                rightPart = nums[middle : len(nums)]
            
                if leftPart[len(leftPart) - 1] >= target:
                    return binary_search(leftPart, left_i, left_i + middle - 1)
                else:
                    return binary_search(rightPart, left_i + middle, right_i)

            return binary_search(nums, 0, len(nums) - 1)