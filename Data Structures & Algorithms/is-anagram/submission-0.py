class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hmap = {}

        for i in range(len(s)):
            hmap[s[i]] = hmap.get(s[i], 0) + 1
            hmap[t[i]] = hmap.get(t[i], 0) - 1
        
        for val in hmap.values():
            if val != 0:
                return False
        return True