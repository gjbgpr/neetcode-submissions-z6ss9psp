class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for index in range(len(s1)):
            s1_counts[ord(s1[index]) - ord('a')] += 1
            s2_counts[ord(s2[index]) - ord('a')] += 1

        matches = 0
        for index in range(26):
            matches += (1 if s1_counts[index] == s2_counts[index] else 0)

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[right]) - ord('a')
            s2_counts[index] += 1
            if s1_counts[index] == s2_counts[index]:
                matches += 1
            elif s1_counts[index] + 1 == s2_counts[index]:
                matches -= 1

            index = ord(s2[left]) - ord('a')
            s2_counts[index] -= 1
            if s1_counts[index] == s2_counts[index]:
                matches += 1
            elif s1_counts[index] - 1 == s2_counts[index]:
                matches -= 1
            left += 1
        return matches == 26