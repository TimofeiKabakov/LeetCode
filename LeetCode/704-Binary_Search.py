# Every step, we divide the amount of possibilities (our range) by 2, which
# is why the time complexity here will be O(logn) - the maximum amount of
# times we can divide n by 2
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        middle = (left + right) // 2
        current = nums[middle]

        while (current != target and left < right):
            if current < target:
                left = middle + 1
            else:
                right = middle - 1
            middle = (left + right) // 2
            current = nums[middle]
            
        if left == right and current != target:
            return -1

        return middle