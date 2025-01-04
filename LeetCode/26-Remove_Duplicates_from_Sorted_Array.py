class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prevIndex = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[prevIndex] = nums[i]
                prevIndex += 1

        return prevIndex
