class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for word in strs:
            srtd = "".join(sorted(word))
            if srtd in hmap:
                hmap[srtd].append(word)
            else:
                hmap[srtd] = [word]
        
        result = []
        for val in hmap.values():
            result.append(val)
        return result