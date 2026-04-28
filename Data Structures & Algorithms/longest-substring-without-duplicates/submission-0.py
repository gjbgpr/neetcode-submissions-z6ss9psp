class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uset = set()
        left = right = 0
        result = 0
        minus_a = ord('a')
        while right < len(s):
            if s[right] in uset:
                result = max(result, right - left)
                while s[right] in uset:
                    uset.remove(s[left])
                    left += 1
            uset.add(s[right])
            right += 1
        result = max(result, right - left)
        return result