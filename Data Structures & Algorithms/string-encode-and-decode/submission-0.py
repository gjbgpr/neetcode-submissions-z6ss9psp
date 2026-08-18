class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for word in strs:
            length = len(word)
            result += str(length) + '#' + word
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        left = right = 0
        while right < len(s):
            while right < len(s) and s[right] != '#': 
                right += 1
            length = int(s[left:right])
            left = right + 1
            right += length + 1
            result.append(s[left:right])
            left = right
        return result