class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        left = result = max_frequency = 0

        for right in range(len(s)):
            hmap[s[right]] = hmap.get(s[right], 0) + 1
            max_frequency = max(max_frequency, hmap[s[right]])

            is_valid = right - left + 1 - max_frequency <= k
            if not is_valid:
                hmap[s[left]] -= 1
                left += 1
            result = max(max_frequency, right - left + 1)
        return result