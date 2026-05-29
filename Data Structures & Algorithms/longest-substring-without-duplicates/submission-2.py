class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hset = set()
        left, right = 0, 0
        longest = 0
        while right < len(s):
            if s[right] in hset:
                longest = max(longest, right - left)
                while s[right] in hset:
                    hset.remove(s[left])
                    left += 1
            hset.add(s[right])
            right += 1
        longest = max(longest, right - left)
        return longest