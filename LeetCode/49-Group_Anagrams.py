class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_dict = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char)- ord('a')] += 1
            
            hash_dict[tuple(count)].append(s)
        
        return list(hash_dict.values())

# Time Complexity: O(n * m)
# Space Complexity: O(n)
# n is the number of strings and m is the average length of the string

# Another Solution (hash()):
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         hash_dict = {}
#         res = []

#         for s in strs:
#             hash_str = 0
            
#             for char in s:
#                 hash_str += hash(char)

#             if hash_str in hash_dict.keys():
#                 hash_dict[hash_str].append(s)
#             else:
#                 hash_dict[hash_str] = [s]
            
#         for hash_val in hash_dict.keys():
#             res.append(hash_dict[hash_val])

#         return res
