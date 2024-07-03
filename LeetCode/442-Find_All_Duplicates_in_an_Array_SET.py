class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        encountered = set()

        for x in nums:
            if x in encountered:
                res.append(x)
            else:
                encountered.add(x)

        return res
    
# Time complexity: O(n)
# Space complexity: O(n)