class Solution:
    def maxSubArray(self, nums) -> int:
        if(len(nums) == 1):
            return nums[0]

        max_sum = nums[0]

        sums = [0] * len(nums)
        sums[0] = nums[0]
        for i in range(1, len(nums)):
            sums[i] = sums[i - 1] + nums[i]

        diff = 0
        min_s = sums[0]
        for i in range(1, len(sums)):
            diff = sums[i] - min_s

            if max_sum < diff:
                max_sum = diff
            
            if max_sum < sums[i]:
                max_sum = sums[i]

            if min_s > sums[i]:
                min_s = sums[i]

        return max_sum
