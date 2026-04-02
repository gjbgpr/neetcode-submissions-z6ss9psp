class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = []
        left = right = 0
        while right < len(s):
            while right < len(s) and s[right] != ' ':
                right += 1
            words.append(s[left:right])
            right += 1
            left = right
                
        if len(words) != len(pattern):
            return False
        
        hmap = {}
        seen = set()
        for i in range(len(pattern)):
            if pattern[i] not in hmap:
                if words[i] not in seen:
                    hmap[pattern[i]] = words[i]
                    seen.add(words[i])
                else:
                    return False
            else:
                if hmap[pattern[i]] != words[i]:
                    return False
        return True