class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumTotal = n * (n + 1) // 2
        counter = 0

        for num in nums:
            counter += num

        return sumTotal - counter
            
