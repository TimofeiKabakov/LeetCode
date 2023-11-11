class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictNums = {}
        for num in nums:
            if num in dictNums:
                return True
            dictNums[num] = 1
        return False
        
