class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_s, hash_t = {}, {}

        for i in range(len(s)):
            hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
            hash_t[t[i]] = 1 + hash_t.get(t[i], 0)

        for letter in hash_s.keys():
            if not hash_t.get(letter) or hash_s[letter] != hash_t[letter]:
                return False

        return True

# Time Complexity: O(n)
# Space Complexity: O(n)