class Solution:
    def canJump(self, nums: List[int]) -> bool:
        haveReached = [False] * len(nums)

        haveReached[0] = True

        for i, n in enumerate(nums):
            if haveReached[i]:
                for jump in range(1, n + 1):
                    if i + jump < len(nums):
                        haveReached[i + jump] = True
                    else:
                        return True
 
        return haveReached[len(haveReached) - 1]
