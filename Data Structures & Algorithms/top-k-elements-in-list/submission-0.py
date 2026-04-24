class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        
        cache = [[] for i in range(len(nums) + 1)]
        print(cache)
        for key, val in hmap.items():
            print(key, val)
            cache[val].append(key)
        
        print(cache)
        result = []
        length = len(cache) - 1
        while k > 0:
            for num in cache[length]:
                if k > 0:
                    result.append(num)
                    k -= 1
                else:
                    break
            length -= 1
        return result