class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            hmap[sorted_word].append(word)
        
        result = []
        for vals in hmap.values():
            result.append(vals)
        
        return result