class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        result_index, result_length = 0, 0

        for i in range(len(s)):
            #even length
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > result_length:
                    result_index = left
                    result_length = right - left + 1
                left -= 1
                right += 1
            
            #odd length
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > result_length:
                    result_index = left
                    result_length = right - left + 1
                left -= 1
                right += 1
        return s[result_index:result_index + result_length]