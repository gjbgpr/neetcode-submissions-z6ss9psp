class Solution:
    def romanToInt(self, s: str) -> int:
        hmap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        right = len(s) - 1
        result = 0
        while (right >= 0):
            curr = hmap[s[right]]
            if right - 1 >= 0 and hmap[s[right - 1]] < curr:
                curr -= hmap[s[right - 1]]
                right -= 1
            result += curr
            right -= 1
        return result