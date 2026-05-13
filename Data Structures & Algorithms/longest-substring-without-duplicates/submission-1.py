class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left, right = 0, 0
        uset = set()
        while right < len(s):
            if s[right] in uset:
                longest = max(longest, right - left)
                while s[right] in uset:
                    uset.remove(s[left])
                    left += 1
            uset.add(s[right])
            right += 1
        longest = max(longest, right - left)
        return longest