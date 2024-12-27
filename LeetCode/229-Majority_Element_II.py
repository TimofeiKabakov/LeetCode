class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash_map = {}
        
        for n in nums:
            hash_map[n] = 1 + hash_map.get(n, 0)
            
            if len(hash_map.values()) <= 2:
                continue
            
            new_hash_map = {}
            for key, value in hash_map.items():
                if hash_map[key] > 1:
                    new_hash_map[key] = value - 1
            hash_map = new_hash_map

        res = []
        for n in hash_map:
            if nums.count(n) > len(nums) // 3:
                res.append(n)

        return res

# Time Complexity: O(n)
# Space Complexity: O(1)