class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for word in strs:
            word_length = len(word)
            result += str(word_length) + '#' + word
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        left = right = 0
        while right < len(s):
            while right < len(s) and s[right] != '#':
                right += 1
            word_length = int(s[left:right])
            left = right + 1
            right += word_length + 1
            result.append(s[left:right])
            left = right
        return result