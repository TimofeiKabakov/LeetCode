class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0] * len(nums)
        self.sums[0] = nums[0]
        for i in range(1, len(nums)):
            self.sums[i] = self.sums[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if not left:
            return self.sums[right]

        return self.sums[right] - self.sums[left - 1]