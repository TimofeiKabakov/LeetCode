class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapNum = {}

        for i, num in enumerate(nums):
            if (target - num in mapNum):
                return [mapNum[target - num], i]
            mapNum[num] = i

        return []
