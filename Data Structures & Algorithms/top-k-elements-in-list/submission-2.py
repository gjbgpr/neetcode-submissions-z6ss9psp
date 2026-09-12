class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, val in hmap.items():
            bucket[val].append(key)
        
        result = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                if k == 0:
                    return result
                result.append(num)
                k -= 1
        return result