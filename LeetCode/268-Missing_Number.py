class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        setNums = set(range(n + 1))
        for num in nums:
            if num in setNums:
                setNums.discard(num)
        return list(setNums)[0]
