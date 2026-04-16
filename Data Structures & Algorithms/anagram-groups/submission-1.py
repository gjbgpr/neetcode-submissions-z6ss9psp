class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for word in strs:
            srtd = "".join(sorted(word))
            hmap[srtd].append(word)
        
        result = []
        for val in hmap.values():
            result.append(val)
        return result