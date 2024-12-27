class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [[] for i in range(len(nums))]
        counts_dict = {}
        res = []

        for num in nums:
            counts_dict[num] = 1 + counts_dict.get(num, 0)

        for key, value in counts_dict.items():
            counts[value - 1].append(key)

        amount = 0
        for i in range(len(counts) - 1, -1, -1):
            for j in range(len(counts[i])):
                amount += 1
                res.append(counts[i][j])

                if amount == k:
                    return res

        return res

# Time Complexity: O(n)
# Space Complexity: O(n)